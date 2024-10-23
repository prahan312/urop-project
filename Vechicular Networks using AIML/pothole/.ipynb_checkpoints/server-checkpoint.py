import socket

# Server configuration
server_ip = "127.0.0.1"
server_port = 12345

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_socket.bind((server_ip, server_port))

print(f"UDP server listening on {server_ip}:{server_port}")

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)

    # Process the received data (in this example, just print it)
    print(f"Received from {client_address}: {data.decode('utf-8')}")

    # Add your logic to handle pothole warnings (store in a database, notify authorities, etc.)
