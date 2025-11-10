from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
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


# @router.post("/chat", response_model=ChatResponse)
# async def chat(request: ChatRequest):
#     chat_service = get_chat_service()
#
#     if not request.session_id:
#         raise HTTPException(status_code=400, detail="session_id є обов'язковим")
#
#     try:
#         result = await chat_service.chat(
#             session_id=request.session_id,
#             message=request.message
#         )
#
#         return ChatResponse(**result)
#
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Помилка: {str(e)}")


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

            await websocket.send_json({
                "type": "start",
                "message": "Обробка запиту..."
            })

            full_response = []
            sources = []

            async for chunk in chat_service.chat_stream(session_id, message):
                if chunk.startswith("\n\n---SOURCES---\n"):
                    sources_json = chunk.replace("\n\n---SOURCES---\n", "")
                    try:
                        sources = json.loads(sources_json)
                    except:
                        pass
                else:
                    full_response.append(chunk)
                    await websocket.send_json({
                        "type": "stream",
                        "content": chunk
                    })

            await websocket.send_json({
                "type": "end",
                "sources": sources,
                "full_response": "".join(full_response)
            })

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
