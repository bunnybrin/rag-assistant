from fastapi import APIRouter
from src.api.dependencies import get_chat_service

router = APIRouter()


# @router.get("/")
# async def root():
#     return {
#         "message": "RAG Assistant API",
#         "docs": "/docs",
#         "health": "/health"
#     }


@router.get("/health")
async def health():
    try:
        get_chat_service()
        chat_active = True
    except:
        chat_active = False

    return {
        "status": "healthy",
        "chat_service": "active" if chat_active else "inactive"
    }
