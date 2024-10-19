# Jaden Ramcharan
# ramc8401@mylaurier.ca
# 169028401
'''
import socket

def start_server():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Bind to localhost on port 12345
    server_socket.listen(1)
    print("Server is listening...")
    
    port = 12345
    for i in range(3):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', port + i))

    while True:
        server_socket.listen(1)
        print("Server is listening...")
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        data = client_socket.recv(1024).decode()
        if data:
            print(f"Received: {data}")
            upcased_data = data + " ACK"
            client_socket.send(upcased_data.encode())

        client_socket.close()

if __name__ == '__main__':
    start_server()
'''

import socket

from threading import Thread


def on_new_client(client_socket, addr):
    while True:
        data = client_socket.recv(1024).decode()
        if data == "exit":
            break
        print(f"{addr} >> {data}")
        upcased_data = data + " ACK"
        client_socket.send(upcased_data.encode())
    client_socket.close()


def main():
    host = 'localHost'  # allow any incoming connections
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))  # bind the socket to the port and ip address

    s.listen(5)  # wait for new connections

    while True:
        c, addr = s.accept()  # Establish connection with client.
        # this returns a new socket object and the IP address of the client
        print(f"New connection from: {addr}")
        thread = Thread(target=on_new_client, args=(c, addr))  # create the thread
        thread.start()  # start the thread
    c.close()
    thread.join()


if __name__ == '__main__':
    main()
