import socket
from scripts.tracker.filter_data import *


def run_tracker():
    s = socket.socket()
    print('Socket Created')
    s.bind(('10.1.4.54', 5000))
    s.listen(3)
    print('Waiting for connections')
    while True:
        try:
            connection, address = s.accept()
            print("Connected with", address)
            try:
                msg_packet = connection.recv(2048).decode()
                print("Message 1st Package: ", msg_packet)
                msg_packet_2 = connection.recv(2048).decode()
                print("Message 2nd Package: ", msg_packet_2)
                get_data(msg_packet_2, address)

            except Exception as e:
                print(str(e))
                connection.close()

        except Exception as e:
            print(str(e))
















