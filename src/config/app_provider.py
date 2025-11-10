from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cached_property

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from src.vectorstore.chroma import ChromaVectorStoreProvider


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    openai_api_key: str = Field(..., description="OpenAI API key")
    chunk_size: int = Field(default=100, gt=0, description="Chunk size for text splitting")
    chunk_overlap: int = Field(default=50, ge=0, description="Chunk overlap for text splitting")
    data_dir: str = Field(default="./data", description="Directory for data files")
    persist_dir: str = Field(default="./storage", description="Directory for persistence")
    persist_dir_vectorstore: str = Field(
        default="./storage/vectordb",
        description="Directory for vector store persistence"
    )
    collections_name: str = Field(default="documents", description="Name of the vector store collection")

    @field_validator("openai_api_key")
    @classmethod
    def validate_api_key(cls, v: str) -> str:
        if not v:
            raise ValueError("OpenAI API key cannot be empty")
        if not v.startswith("sk-"):
            raise ValueError("OpenAI API key must start with 'sk-'")
        return v

    @field_validator("chunk_overlap")
    @classmethod
    def validate_chunk_overlap(cls, v: int, info) -> int:
        chunk_size = info.data.get("chunk_size", 50)
        if v >= chunk_size:
            raise ValueError(f"chunk_overlap ({v}) must be less than chunk_size ({chunk_size})")
        return v


class ServiceFactory:
    def __init__(self, settings: AppSettings):
        self._settings = settings

    @cached_property
    def llm(self) -> OpenAI:
        return OpenAI(
            model="gpt-4o",
            temperature=0,
            api_key=self._settings.openai_api_key,
        )

    @cached_property
    def embedding_model(self) -> OpenAIEmbedding:
        return OpenAIEmbedding(
            model="text-embedding-3-small",
            api_key=self._settings.openai_api_key,
            dimensions=1536,
        )

    @cached_property
    def vectorstore(self) -> ChromaVectorStoreProvider:
        return ChromaVectorStoreProvider(
            collections_name="llama_index",
            persist_dir_vectorstore=self._settings.persist_dir_vectorstore,
            persist_dir_storage=self._settings.persist_dir,
        )


app_settings = AppSettings()
service_factory = ServiceFactory(app_settings)
