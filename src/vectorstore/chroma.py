from llama_index.core import  StorageContext, load_index_from_storage
from llama_index.core.indices.base import BaseIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb


class ChromaVectorStoreProvider:
    def __init__(self, collections_name, persist_dir_vectorstore, persist_dir_storage):
        self.collection_name = collections_name
        self.persist_dir_vectorstore = persist_dir_vectorstore
        self.persist_dir_storage = persist_dir_storage

    def _get_chroma_client(self):
        return chromadb.PersistentClient(path=str(self.persist_dir_vectorstore))

    def get_vector_store(self) -> ChromaVectorStore:
        chroma_client = self._get_chroma_client()
        chroma_collection = chroma_client.get_or_create_collection(self.collection_name)
        return ChromaVectorStore(chroma_collection=chroma_collection)

    def load_index(self) -> BaseIndex:
        vector_store = self.get_vector_store()

        storage_context = StorageContext.from_defaults(
            vector_store=vector_store,
            persist_dir=str(self.persist_dir_storage)
        )

        index = load_index_from_storage(storage_context)

        return index

    def index_exists(self) -> bool:
        return True


    def get_collection_count(self) -> int:
        try:
            chroma_client = self._get_chroma_client()
            chroma_collection = chroma_client.get_collection(self.collection_name)
            return chroma_collection.count()
        except:
            return 0
