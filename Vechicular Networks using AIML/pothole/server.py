import socket

# Server configuration
server_ip = "127.0.0.1"
server_port = 12345

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_socket.bind((server_ip, server_port))

print(f"UDP server listening on {server_ip}:{server_port}")

# Dictionary to store connected clients
connected_clients = {}

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)

    # Process the received data
    message = data.decode('utf-8')
    print(f"Received from {client_address}: {message}")

    # Check if the client is in the dictionary
    if client_address not in connected_clients:
        # Create a new socket for the client
        connected_clients[client_address] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Retransmit the message to other clients if it contains "Pothole detected"
    if "Pothole detected" in message:
        for other_client_address, other_client_socket in connected_clients.items():
            if other_client_address != client_address:
                try:
                    other_client_socket.sendto(data, other_client_address)
                    print(f"Retransmitted to {other_client_address}: {message}")
                except Exception as e:
                    print(f"Error retransmitting to {other_client_address}: {e}")

    # Print connected clients for debugging
    print("Connected Clients:", connected_clients)
