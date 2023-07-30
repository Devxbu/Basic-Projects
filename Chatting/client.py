import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

def main():
    # Creating the socket class object
    # AF_INET: we are going to use IPv4 adress
    # SOCK_STREAM: we are using TCP packets for communication
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server 
    try:
        client.connect((HOST, PORT))
        print(f"Connected to host {HOST} and port {PORT}")
    except:
        print(f"Unable to connect to host {HOST} and port {PORT}")
if __name__ ==  '__main__':
    main()