from dataclasses import dataclass

from src.config import app_settings, service_factory
from src.indexing.indexer import DocumentIndexer


@dataclass
class IndexResult:

    num_documents: int
    success: bool
    message: str


class IndexingService:
    def index_documents(self) -> IndexResult:
        indexer = DocumentIndexer()

        indexer.index_documents()

        return IndexResult(
            num_documents=0,
            success=True,
            message=f"Successfully indexed nodes",
        )

    def get_index_status(self) -> dict:
        exists = service_factory.vectorstore.index_exists()
        total_docs = 0

        if exists:
            try:
                total_docs = service_factory.vectorstore.get_collection_count()
            except Exception:
                pass

        return {
            "exists": exists,
            "total_documents": total_docs,
            "collection_name": app_settings.collections_name,
            "persist_dir": app_settings.persist_dir,
        }
