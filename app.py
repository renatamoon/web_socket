# STANDARD IMPORTS
import asyncio
import websockets


connected = set()


async def server(websocket, path):
    # register
    connected.add(websocket)

    try:
        async for message in websocket:
            for conn in connected:
                if conn != websocket:
                    await conn.send(f"Got a new message for you: {message}")
    finally:
        # UNREGISTER
        connected.remove(websocket)

start_server = websockets.serve(server, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
