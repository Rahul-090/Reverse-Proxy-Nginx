import asyncio
import websockets

# Function to handle receiving messages from the WebSocket server
async def receive_message(websocket):
    try:
        # Receive messages from the WebSocket server
        async for message in websocket:
            print(f"Received message from User 1 server: {message}")
    except websockets.exceptions.ConnectionClosedError:
        print("WebSocket connection closed for User 1")

# Connect to the WebSocket server for User 1
async def connect_to_user1_server():
    async with websockets.connect("ws://localhost:8765") as websocket_user1:
        print("Connected to User 1 WebSocket server")
        await receive_message(websocket_user1)

# Run the WebSocket client for User 1
asyncio.run(connect_to_user1_server())
