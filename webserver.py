#import socket module
from socket import *
import sys # In order to terminate the program
import threading

def client_handler(connectionSocket, connection_addr):
    message = connectionSocket.recv(1024).decode()
    print('\n')
    print("NEW CONNECTION FROM CLIENT AT:", connection_addr[0], connection_addr[1])
    print("HANDLED ON:", threading.currentThread())
    # print("FROM CLIENT:", message)
    # Add code to check message so the split and index below does not
    # cause your webserver to crash.
    # Or, do the split separately and then check the list returned by split
    try:
        list = message.split()
        if (len(list) > 1):
            filename = list[1] # /HelloWorld.html
            print("File requested from client: " + filename)
            f = open(filename[1:])
            outputdata = f.read().split("\r\n")
            #Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\n".encode())
            print("SERVER RESPONSE: HTTP/1.1 200 OK")
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
        else:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\n<html><body>404 Not Found</body></html>".encode())
            print("SERVER RESPONSE: HTTP/1.1 404 Not Found")
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\n<html><body>404 Not Found</body></html>".encode())
        print("SERVER RESPONSE: HTTP/1.1 404 Not Found")
        #Close connection socket
        connectionSocket.close()

def run_server():
    serverIP = gethostbyname(gethostname())
    print("Host IP address: " + serverIP) #192.168.2.215
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
    SERVER_PORT = 12000
    print("Listening at: " + str(SERVER_PORT))
    serverSocket.bind(("", SERVER_PORT))
    serverSocket.listen(5)
    print('Ready to serve...')
    threads = []
    bool = True
    while bool:
        #Establish the connection
        try:
            connectionSocket, addr = serverSocket.accept()
            t = threading.Thread(target = client_handler,
                                 args = (connectionSocket, addr))
            threads.append(t)
            t.start()
        except KeyboardInterrupt:
            bool = False

    serverSocket.close()
    print("Server socket closing...")
    sys.exit() #Terminate the program after sending the corresponding data

if __name__ == "__main__":
    run_server()
