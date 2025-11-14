from llama_index.core.chat_engine import ContextChatEngine
from llama_index.core.memory import ChatMemoryBuffer

from single_query import retriever, synth

memory = ChatMemoryBuffer.from_defaults(token_limit=4096)

chat_engine = ContextChatEngine.from_defaults(
    retriever=retriever,
    memory=memory,
    response_synthesizer=synth,
    system_prompt="Ти - помічник, який надає відповіді на основі наданих документів. "
                  "Завжди посилайся на конкретні джерела в своїх відповідях. "
                  "Якщо користувач посилається на попередню відповідь (наприклад, 'пункт 2', 'документ який ти згадав'), "
                  "використовуй інформацію з історії розмови для точної відповіді."
)

print("ПИтання 1:")
resp1 = chat_engine.chat("з яких джерел ти можеш надати інформацію?")
print("Відповідь 1:")
print(resp1)

print("ПИтання 2:")
resp2 = chat_engine.chat("Роскажи про документ наведений в 2 пункті")
print("\nВідповідь 2:")
print(resp2)