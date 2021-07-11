from socket import *
import sys

SERVER_NAME = 'localhost'  #127.0.0.1 #serverhost: 192.168.2.215
SERVER_PORT = 12000

def run_client(server_name, server_port, filename):
    client_socket = socket(AF_INET, SOCK_STREAM) # create the socket, IPv4, TCP
    try:
        client_socket.connect((server_name, server_port)) # a tuple of the host name/IP address and port
    except Exception as e:
        print("Unable to connect, please check correct server host and port")
        sys.exit()
    message = "GET /" + filename + " HTTP/1.1\r\n"
    client_socket.send(message.encode())
    response = client_socket.recv(1024)
    print("\nSERVER RESPONSE: " + response.decode())
    print("AT: ", client_socket.getpeername())
    print("\n")
    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: client.py [server_host] [server_port] [filename]")
        sys.exit()
    else:
        sn = sys.argv[1]
        sp = int(sys.argv[2])
        fn = sys.argv[3]
    run_client(sn, sp, fn)
