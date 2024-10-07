import asyncio
import websockets
import time

async def test_server_b():
    uri = "ws://tuip:8765"  # IP pública del servidor B
    while True:  # Bucle para reintentar indefinidamente
        try:
            async with websockets.connect(uri) as websocket:
                print("Conectado al servidor B")
                while True:
                    message = await websocket.recv()
                    print(f"Mensaje recibido del servidor B: {message}")
        except Exception as e:
            print(f"Error al conectar con el servidor B: {e}")
            print("Reintentando en 1 segundo...")
            await asyncio.sleep(1)  # Espera 1 segundo antes de intentar reconectar

# Ejecuta la función para intentar reconectar indefinidamente
asyncio.get_event_loop().run_until_complete(test_server_b())
