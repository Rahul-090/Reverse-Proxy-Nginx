import asyncio
import websockets

# Function to handle receiving messages from the WebSocket server
async def receive_message(websocket):
    try:
        # Receive messages from the WebSocket server
        async for message in websocket:
            print(f"Received message from User 2 server: {message}")
    except websockets.exceptions.ConnectionClosedError:
        print("WebSocket connection closed for User 2")

# Connect to the WebSocket server for User 2
async def connect_to_user2_server():
    async with websockets.connect("ws://localhost:8766") as websocket_user2:
        print("Connected to User 2 WebSocket server")
        await receive_message(websocket_user2)

# Run the WebSocket client for User 2
asyncio.run(connect_to_user2_server())
