import asyncio
import websockets
from googletrans import Translator

# Translator instance
translator = Translator()

# Set to store active WebSocket clients
clients = set()

async def handle_connection(websocket, path):
    """Handle incoming WebSocket connections."""
    clients.add(websocket)
    try:
        async for message in websocket:
            # Translate message to Spanish
            translated_message = translator.translate(message, dest="es").text
            print(f"Received: {message} | Translated: {translated_message}")

            # Broadcast the translated message to all connected clients
            for client in clients:
                if client != websocket:  # Don't send the message back to the sender
                    await client.send(translated_message)
    except websockets.ConnectionClosed:
        print("Client disconnected")
    finally:
        clients.remove(websocket)

async def main():
    """Start the WebSocket server."""
    server = await websockets.serve(handle_connection, "localhost", 8765)
    print("WebSocket server is running on ws://localhost:8765")

    try:
        await asyncio.Future()  # Run forever
    except asyncio.CancelledError:
        print("\nShutting down WebSocket server...")
        server.close()
        await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
