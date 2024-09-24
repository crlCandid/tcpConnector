import socket
from classes.client import Client
from datetime import datetime

# host = input('Set Host: ')
# port = int(input('Set Port: '))  

host = 'localhost'
port = 3999
buffer = 4096
clients = []

def NewClient( socket, address):
    clients.append(Client(address, socket))
    print(f"New Client: {address}")

def MsgBuilder( data, client) -> str:
    result = f"""
====================START================
At: {datetime.now()}
====================MSG==================
{data}
====================END OF MSG==========="""
    return result

try:
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind((host, port))
    connection.listen()
    connection.setblocking(False)
    print(f"Server listening on {host}:{port}")
except socket.error as e:
    print(f"Socket error: {e}")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()


while True:
    try:
        client_socket, client_address = connection.accept()
        NewClient(client_socket, client_address)
    except BlockingIOError:
        pass

    for client in clients:
        try:
            data = client.Socket.recv(buffer).decode()
            if data:
                f = open(f"log-{client.Address}.txt", "a")
                msg = MsgBuilder(data, client)
                f.write(msg + '\n')
                f.close()
                print(msg)
                continue
            
            if not data:
                print(f"Disconnect from client {client.Address}")
                clients.remove(client)
        except BlockingIOError:
            pass
        except ConnectionResetError:
            print("Connection closed by client.")