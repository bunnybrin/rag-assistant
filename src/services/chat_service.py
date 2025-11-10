import json
from typing import AsyncIterator, Dict, List

from llama_index.core.chat_engine.types import ChatMode, BaseChatEngine
from llama_index.core.indices.base import BaseIndex

from src.retrieval.citations import CitationExtractor

SOURCES_MARKER = "\n\n---SOURCES---\n"


class ChatService:
    def __init__(self, index: BaseIndex):
        self.index = index
        self.citation_extractor = CitationExtractor()
        self._chat_engines: Dict[str, BaseChatEngine] = {}

    def _get_or_create_chat_engine(self, session_id: str):
        if session_id not in self._chat_engines:
            self._chat_engines[session_id] = self.index.as_chat_engine(
                chat_mode=ChatMode.CONDENSE_PLUS_CONTEXT,
                similarity_top_k=5,
                streaming=True,
                verbose=True
            )
        return self._chat_engines[session_id]

    def _extract_sources(self, response) -> List[Dict]:
        if hasattr(response, 'source_nodes') and response.source_nodes:
            return self.citation_extractor.extract_sources(response.source_nodes)
        return []

    # async def chat(self, session_id: str, message: str) -> Dict:
    #     try:
    #         chat_engine = self._get_or_create_chat_engine(session_id)
    #         response = chat_engine.chat(message)
    #
    #         return {
    #             "response": str(response),
    #             "sources": self._extract_sources(response),
    #             "session_id": session_id
    #         }
    #     except Exception as e:
    #         raise RuntimeError(f"Помилка під час обробки повідомлення: {str(e)}")

    async def chat_stream(self, session_id: str, message: str) -> AsyncIterator[str]:
        try:
            chat_engine = self._get_or_create_chat_engine(session_id)
            streaming_response = chat_engine.stream_chat(message)

            for text in streaming_response.response_gen:
                yield text

            sources = self._extract_sources(streaming_response)
            yield SOURCES_MARKER
            yield json.dumps(sources, ensure_ascii=False)
        except Exception as e:
            yield f"\n\nПомилка: {str(e)}"

    def delete_session(self, session_id: str):
        if session_id in self._chat_engines:
            del self._chat_engines[session_id]
