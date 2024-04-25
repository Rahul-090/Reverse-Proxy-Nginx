<h2>Configure reverse proxy to access docker containers</h2>

1. Nginx Container: Configured as a reverse proxy to map the URL path to the 
corresponding IP addresses.
2. Responder 1 Container: Runs a WebSocket server and sends "Hello from <IP address 
of the container>!" messages to connected clients every 5 seconds.
3. Responder 2 Container: Functions identically to the Responder 1 Container.
