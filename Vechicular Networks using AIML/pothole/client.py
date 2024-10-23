import socket
import time
# Server configuration
server_ip = "127.0.0.1"
server_port = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the client socket to a specific address and port
client_ip = "127.0.0.2"  # Replace with the actual client IP
client_port = 54321  # Choose a unique port for the client
client_socket.bind((client_ip, client_port))

print(f"UDP client listening on {client_ip}:{client_port}")

# Send a message to the server
message = "Hello from client"
client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))
print(f"Sent message to server {server_ip}:{server_port}: {message}")

# Receive a response from the server
response, server_address = client_socket.recvfrom(1024)
print(f"Received response from server {server_address}: {response.decode('utf-8')}")
time.sleep(5)

# Close the socket
client_socket.close()

# Stop the client after receiving a response
print("Client stopped.")
