from typing import List
from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import (
    SentenceSplitter,
)
from llama_index.core import VectorStoreIndex, StorageContext

from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore

from src.config.app_provider import  app_provider


class DocumentIndexer:

    def __init__(self):
        self._create_pipeline()

    def _create_pipeline(self):
        transformations = [
            SentenceSplitter(
                chunk_size=app_provider.chunk_size,
                chunk_overlap=app_provider.chunk_overlap
            ),
            app_provider.embedding_model
        ]

        self.pipeline = IngestionPipeline(
            transformations=transformations,
            vector_store=app_provider.vectorstore.get_vector_store()
        )

    def load_documents(self) -> List[Document]:
        print(f"📚 Завантаження документів з {app_provider.data_dir}...")

        reader = SimpleDirectoryReader(
            input_dir=app_provider.data_dir,
            recursive=True,
            required_exts=[".pdf", ".txt", ".md", ".docx"]
        )

        documents = reader.load_data()
        print(f"✅ Завантажено {len(documents)} документів")

        return documents

    def index_documents(self):
        documents = self.load_documents()

        print("🔄 Обробка документів через IngestionPipeline...")

        nodes = self.pipeline.run(
            documents=documents,
            show_progress=True
        )

        vector_store = app_provider.vectorstore.get_vector_store()

        docstore = SimpleDocumentStore()
        index_store = SimpleIndexStore()

        storage_context = StorageContext.from_defaults(
            docstore=docstore,
            index_store=index_store,
            vector_store=vector_store,
            persist_dir=app_provider.persist_dir,
        )

        storage_context.docstore.add_documents(nodes)

        index = VectorStoreIndex(
            nodes=nodes,
            storage_context=storage_context,
            show_progress=False,
            store_nodes_override=True
        )

        index.storage_context.persist()

        print("\n" + "=" * 60)
        print("✅ ІНДЕКСАЦІЯ ЗАВЕРШЕНА")
        print("=" * 60 + "\n")
        return len(nodes)
