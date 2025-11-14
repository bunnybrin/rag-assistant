from llama_index.core.chat_engine import ContextChatEngine
from llama_index.core.memory import ChatMemoryBuffer

from single_query import retriever, synth
from src.config.chat_prompts import system_prompt, context_template, context_refine_template

memory = ChatMemoryBuffer.from_defaults(token_limit=4096)

chat_engine = ContextChatEngine.from_defaults(
    retriever=retriever,
    memory=memory,
    response_synthesizer=synth,
    system_prompt=system_prompt,
    context_template=context_template,
    context_refine_template=context_refine_template
)

print("ПИтання 1:")
resp1 = chat_engine.chat("з яких джерел ти можеш надати інформацію?")
print("Відповідь 1:")
print(resp1)

print("ПИтання 2:")
resp2 = chat_engine.chat("Роскажи про документ наведений в 2 пункті")
print("\nВідповідь 2:")
print(resp2)

print("ПИтання 3:")
resp2 = chat_engine.chat("Роскажи про Глебену")
print("\nВідповідь 3:")
print(resp2)