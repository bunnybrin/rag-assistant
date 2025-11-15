from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from llama_cloud_services import LlamaCloudIndex

from src.config import app_settings
from src.services.chat_service import ChatService
from src.api.dependencies import set_chat_service
from src.api.routes import chat, system, pipelines


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Run RAG Assistant API...")
    chat_service = ChatService(LlamaCloudIndex(
        name="appalling-bass-2025-11-11",
        project_name="Default",
        organization_id="6a4701a8-5d2f-4a92-a8fa-8f8089062598",
        api_key=app_settings.llama_cloud_api_key,
    ))
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

app.include_router(pipelines, prefix="/api", tags=["pipelines"])

try:
    app.mount("/", StaticFiles(directory="ui/dist", html=True), name="static")
except RuntimeError:
    print("⚠️ Static not found")
