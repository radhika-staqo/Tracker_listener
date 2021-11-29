import socket
import threading
from scripts.tracker.filter_data import *


def listener():
    s = socket.socket()
    print('Socket Created')
    s.bind(('10.1.4.54', 5000))
    s.listen(300)
    while True:
        connection, address = s.accept()
        connection.settimeout(10)
        thread = threading.Thread(target=listen_to_device, args=(connection, address))
        thread.start()
        print("Connection Established")


def listen_to_device(connection, address):
    size = 32768
    status = True
    while status:
        try:
            msg_packet = connection.recv(size).decode()
            print("Message 1st Package: ", msg_packet)
            msg_packet = msg_packet.replace('"', '\\"')
            get_data(msg_packet, address)
            msg_packet_2 = connection.recv(size).decode()
            print("Message 2nd Package: ", msg_packet_2)
            msg_packet_2 = msg_packet_2.replace('"', '\\"')
            get_data(msg_packet_2, address)
        except Exception as e:
            print(str(e))
            status = False
            connection.close()
