
# listener
import socket

s = socket.socket()
print('Socket Created')

s.bind(('192.168.0.103', 6060))


s.listen(3)
print('Waiting for connections')


while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    msg = c.recv(2048).decode()
    print("Connected with", addr, name, msg)
    c.send(bytes('Welcome to myServer', 'utf-8'))

    c.close()















