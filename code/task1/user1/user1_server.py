import asyncio
import websockets
import socket

# Function to get the IP address of the container
def get_container_ip():
    return socket.gethostbyname(socket.gethostname())

# Define the WebSocket server handler
async def websocket_handler(websocket, path):
    print(f"WebSocket connection established for User 1")

    try:
        # Keep the WebSocket connection open
        while True:
            # Get the IP address of the container
            container_ip = "192.168.1.251"

            # Construct the message with the IP address
            message = f"Hello from {container_ip}!"

            # Send the message to the client
            await websocket.send(message)

            # Wait for 5 seconds before sending the next message
            await asyncio.sleep(5)

    except websockets.exceptions.ConnectionClosedError:
        print(f"WebSocket connection closed for User 1")

# Start the WebSocket server for User 1
async def start_user1_server():
    server = await websockets.serve(websocket_handler, "localhost", 8765)
    print("WebSocket server for User 1 started")
    await server.wait_closed()

# Run the WebSocket server for User 1
asyncio.run(start_user1_server())
