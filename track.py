import socket
import sys
import time
import re
import os

os.system('cls')

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
# localhost = "127.0.0.1"
localhost = "0.0.0.0"
port = int("6060")
server_address = (localhost, port)

def echo_server():

    imei = []

    print(sys.stderr, 'starting up on %s port %s' % server_address)

    sock.bind(server_address)
    sock.listen(1)
    print(sock)
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    print('hi')
    print(sys.stderr, 'client connected:', client_address)
    data = connection.recv(1024)


    if data.find('##') > -1:

        imei.append(data)
        print(sys.stderr, 'received %s' % data)

        for line in imei:
            imeidevice = re.sub("\D",'', line)
            id = '0%s' %imeidevice[4:15]

        print(sys.stderr, 'sending  msg to client: LOAD')
        message = 'LOAD'
        connection.sendall(message)


        while True:

            ansdev = connection.recv(1024)
            print(sys.stderr, 'received %s' % ansdev)

            if len(ansdev) == 16:

                #message = '**,imei:%s,B;' %id
                message = 'ON'

                print(sys.stderr, 'sending  msg to client: %s' %message)
                connection.sendall(message)

                ansdev = connection.recv(1024)
                print(sys.stderr, 'received %s' % ansdev)

    connection.close()

def main():

    echo_server()


if __name__ == '__main__':
    main()


























