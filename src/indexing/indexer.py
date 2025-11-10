from typing import List
from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.extractors import SummaryExtractor, QuestionsAnsweredExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import (
    SentenceSplitter,
)
from llama_index.core import VectorStoreIndex, StorageContext

from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore

from src.config import app_settings, service_factory

DEFAULT_SUMMARY_EXTRACT_TEMPLATE = """
Ось зміст розділу:
{context_str}

Підсумуйте основні теми та поняття розділу. 

Підсумок: """


DEFAULT_QUESTION_GEN_TMPL = """\
Ось контекст:
{context_str}

З огляду на контекстну інформацію, \
створіть {num_questions} питань, на які цей контекст може надати \
конкретні відповіді, які навряд чи можна знайти деінде.

Також можуть бути надані більш загальні резюме навколишнього контексту. \
Спробуйте використовувати ці резюме, щоб створити кращі питання, \
на які цей контекст може відповісти.

"""

class DocumentIndexer:

    def __init__(self):
        self._create_pipeline()

    def _create_pipeline(self):
        transformations = [
            SentenceSplitter(
                chunk_size=app_settings.chunk_size,
                chunk_overlap=app_settings.chunk_overlap
            ),
            SummaryExtractor(prompt_template=DEFAULT_SUMMARY_EXTRACT_TEMPLATE),
            QuestionsAnsweredExtractor(prompt_template=DEFAULT_SUMMARY_EXTRACT_TEMPLATE, ),
            service_factory.embedding_model
        ]

        self.pipeline = IngestionPipeline(
            transformations=transformations,
            vector_store=service_factory.vectorstore.get_vector_store()
        )

    def load_documents(self) -> List[Document]:
        print(f"📚 Завантаження документів з {app_settings.data_dir}...")

        reader = SimpleDirectoryReader(
            input_dir=app_settings.data_dir,
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

        vector_store = service_factory.vectorstore.get_vector_store()

        docstore = SimpleDocumentStore()
        index_store = SimpleIndexStore()

        storage_context = StorageContext.from_defaults(
            docstore=docstore,
            index_store=index_store,
            vector_store=vector_store,
            persist_dir=app_settings.persist_dir,
        )

        storage_context.docstore.add_documents(nodes)

        index = VectorStoreIndex(
            nodes=nodes,
            storage_context=storage_context,
            embed_model=service_factory.embedding_model,
            show_progress=False,
            store_nodes_override=True
        )

        index.storage_context.persist()

        print("\n" + "=" * 60)
        print("✅ ІНДЕКСАЦІЯ ЗАВЕРШЕНА")
        print("=" * 60 + "\n")
        return len(nodes)
