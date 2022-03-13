import socket

HOST = "127.0.0.1" # Standard loopback interface address (localhost)
PORT_NUMBER = 65432 # Port to listen on (non-privileged ports are > 1023)

# Initializing server socket with params
# AF_INET: specifying to use an IPv4 address
# SOCK_STREAM: spacifying to use a stream socket, e.g., TCP

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow quick restarts
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Use host and port to bind server socket to the server
server_socket.bind((HOST, PORT_NUMBER))

# Start listening for incoming connections
server_socket.listen()

print(f"\Server started at address {HOST}:{PORT_NUMBER}\n")

# Wait for connection
connection, address = server_socket.accept()

print(f"Client connected from: {address}\n")

# Use an infinite loop to keep server running

while True:
    # Wait to receive a message from the client
    
    data = connection.recv(1024)

    # If no data is received, the client has disconnected
    if not data: break

    # Print received data
    print("--- Received Message from client: ---\n")
    print(data.decode())
    print("--- End of received message --- \n")

    # Create a text response message
    response = "The server got your message: " + data.decode()

    # Send the response to the client
    connection.send(response.encode())

    # Print the sent message
    print("--- Response sent from the server: ---\n")
    print(response)
    print("--- End of server response ---\n")

    # Closing all connections:
    connection.close()
    server_socket.close()

    # Stop the infinite server loop
    break
