from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List, Dict
import json
import uuid

from src.api.dependencies import get_chat_service

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    session_id: str = None


class ChatResponse(BaseModel):
    response: str
    sources: List[Dict]
    session_id: str


@router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    chat_service = get_chat_service()

    session_id = str(uuid.uuid4())
    print(f"Нова сесія створена: {session_id}")

    try:
        await websocket.send_json({
            "type": "session",
            "session_id": session_id
        })

        while True:
            data = await websocket.receive_text()

            try:
                message_data = json.loads(data)
                message = message_data.get("message", "")
            except json.JSONDecodeError:
                message = data

            if not message:
                await websocket.send_json({
                    "type": "error",
                    "message": "Повідомлення порожнє"
                })
                continue

            async for chunk in chat_service.stream_chat(session_id, message):
                await websocket.send_json(chunk)

    except WebSocketDisconnect:
        print(f"WebSocket відключено для сесії {session_id}")
    except Exception as e:
        print(f"Помилка WebSocket: {str(e)}")
        try:
            await websocket.send_json({
                "type": "error",
                "message": f"Помилка: {str(e)}"
            })
        except:
            pass
    finally:
        print(f"Видалення сесії: {session_id}")
        chat_service.delete_session(session_id)
