import os
from typing import Optional

from dotenv import load_dotenv
from dataclasses import dataclass

from functools import cached_property

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from src.utils.helpers import singleton
from src.vectorstore.chroma import ChromaVectorStoreProvider

load_dotenv()


@singleton
@dataclass
class AppProvider:
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    chunk_size: int = 50
    chunk_overlap: int = 50
    data_dir: str = "./data"
    persist_dir: str = "./storage"
    persist_dir_vectorstore: str = "./storage/vectordb"
    collections_name: str = os.getenv("COLLECTIONS_NAME", 'documents')

    @cached_property
    def llm(self):
        return OpenAI(
            model='gpt-4o',
            temperature=0,
            api_key=self.openai_api_key,
        )

    @cached_property
    def embedding_model(self):
        return OpenAIEmbedding(
            model='text-embedding-3-small',
            api_key=self.openai_api_key,
            dimensions=1536,
        )

    @cached_property
    def vectorstore(self):
        return ChromaVectorStoreProvider(
            collections_name="llama_index",
            persist_dir_vectorstore=self.persist_dir_vectorstore,
            persist_dir_storage=self.persist_dir,
        )

app_provider = AppProvider()
