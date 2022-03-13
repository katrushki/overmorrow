import socket

HOST = "127.0.0.1" # standard loopback interface address (localhost)
PORT_NUMBER = 65432 # port to listen on (non-priviledged ports are > 1023)

# Initialize a server socket with the following parameters:
# AF_INET: specifying to use an IPV4 address
# SOCK_STREAM: spacifying to use a stream socket, e.g., TCP

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# allow the societ to quickly restart
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# use host and port (defined above) to bind the server socket to the serbr