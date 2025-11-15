from typing import Dict, AsyncGenerator
from llama_index.core.indices.managed import BaseManagedIndex

from src.engine.chat_engine import ChatEngine


class ChatService:
    def __init__(self, index: BaseManagedIndex):
        self._chat_engines: Dict[str, ChatEngine] = {}
        self.index = index

    def _get_or_create_chat_engine(self, session_id: str):
        if session_id not in self._chat_engines:
            self._chat_engines[session_id] = ChatEngine(self.index)

        return self._chat_engines[session_id]

    async def chat(self, session_id: str, message: str) -> Dict:
        chat_engine = self._get_or_create_chat_engine(session_id)
        response = chat_engine.chat(message)

        return {
            'response': response.response,
            'sources': list(map(lambda x: x.model_dump(), response.source_nodes)),
            'session_id': session_id
        }

    async def stream_chat(self, session_id: str, message: str) -> AsyncGenerator[Dict, None]:
        chat_engine = self._get_or_create_chat_engine(session_id)
        streaming_response = chat_engine.stream_chat(message)

        for token in streaming_response.response_gen:
            yield {
                'type': 'token',
                'content': token,
                'session_id': session_id
            }

        yield {
            'type': 'end',
            'sources': list(map(lambda x: x.model_dump(), streaming_response.source_nodes)),
            'session_id': session_id
        }

    def delete_session(self, session_id: str):
        if session_id in self._chat_engines:
            del self._chat_engines[session_id]
