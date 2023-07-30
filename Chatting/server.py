import socket
import threading

HOST = "127.0.0.1"
PORT = 1234
LISTENER_LIMIT = 5


def main():
    # Creating the socket class object
    # AF_INET: we are going to use IPv4 adress
    # SOCK_STREAM: we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try catch block
    try:
        # Provide the server with an address in the form of
        # host IP and port
        server.bind((HOST, PORT))
        print(f"Binded to host {HOST} and port {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")
        server.listen(5)

    # Set server limit
    server.listen(LISTENER_LIMIT)

    # This while loop will keep listening to client connections
    while 1:
        client, address = server.accept()
        print(f"Succesfully connected to client {address[0]} {address[1]}")

    if __name__ == "__name__":
        main()
