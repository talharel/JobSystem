from fastapi import WebSocket


class WebSocketManager:
    def __init__(self):
        self.connection = None

    async def connect(self, websocket: WebSocket):
        self.connection = websocket
        await websocket.accept()

    async def disconnect(self):
        self.connection = None

    async def send_message(self, message):
        if self.connection:
            await self.connection.send_text(message)


manager = WebSocketManager()
