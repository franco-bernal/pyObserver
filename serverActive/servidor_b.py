import asyncio
import websockets

# Función que envía mensajes cada cierto tiempo al cliente (Servidor A)
async def health_check(websocket, path):
    try:
        while True:
            await websocket.send("Servidor B activo")  # Mensaje que indica que está activo
            await asyncio.sleep(5)  # Envía el mensaje cada 5 segundos
    except websockets.ConnectionClosed:
        print("Conexión cerrada con el cliente")

# Inicia el servidor WebSocket en el puerto 8765
start_server = websockets.serve(health_check, "0.0.0.0", 8765)

# Corre el servidor WebSocket
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
