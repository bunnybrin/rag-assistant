from llama_index.core.chat_engine import ContextChatEngine
from llama_index.core.indices.managed import BaseManagedIndex
from llama_index.core.memory import ChatMemoryBuffer

from src.config.chat_prompts import system_prompt, context_template, context_refine_template


class ChatEngine:
    def __init__(self, index: BaseManagedIndex, ):
        self.memory = ChatMemoryBuffer.from_defaults(token_limit=4096)

        self.retriever = index.as_retriever(similarity_top_k=30, rerank_top_n=10, enable_reranking=True,
                                            retrieval_mode='chunks')

        self.chat_engine = ContextChatEngine.from_defaults(
            retriever=self.retriever,
            memory=self.memory,
            system_prompt=system_prompt,
            context_template=context_template,
            context_refine_template=context_refine_template
        )

    def chat(self, message: str):
        return self.chat_engine.chat(message)

    def stream_chat(self, message: str):
        return self.chat_engine.stream_chat(message)
