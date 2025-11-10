from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.config import service_factory
from src.services.indexing_service import IndexingService
from src.services.chat_service import ChatService
from src.api.dependencies import set_chat_service
from src.api.routes import chat, system


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Run RAG Assistant API...")

    if service_factory.vectorstore.index_exists():
        print("✅ Load existing індексу...")
        indexing_service = IndexingService()
        index = indexing_service.load_existing_index()
    else:
        print("❌ Index not found. Please run indexing first")
        raise RuntimeError("Index not found. Please run indexing first.")

    chat_service = ChatService(index)
    set_chat_service(chat_service)
    print("✅ Chat Service initialized")

    yield

    print("👋 Stop API...")


app = FastAPI(
    title="RAG Assistant API",
    description="API для спілкування з вашими документами через RAG",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(system, tags=["system"])
app.include_router(chat, prefix="/api", tags=["chat"])

try:
    app.mount("/", StaticFiles(directory="static", html=True), name="static")
except RuntimeError:
    print("⚠️ Static not found")
