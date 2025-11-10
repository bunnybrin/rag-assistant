from src.services.chat_service import ChatService


_chat_service_instance: ChatService = None


def set_chat_service(service: ChatService):
    global _chat_service_instance
    _chat_service_instance = service


def get_chat_service() -> ChatService:
    if _chat_service_instance is None:
        raise RuntimeError("Chat service not initialized")
    return _chat_service_instance
