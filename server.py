
# listener
import socket
import re
import mysql.connector


def imei(n):
    if (len(n) == 15):
        return True
    else:
        return False

s = socket.socket()
print('Socket Created')

s.bind(('10.1.4.54', 5000))


s.listen(3)
print('Waiting for connections')


while True:
    try:
        c, addr = s.accept()
    except Exception as e:
        print(e)
    #data = b''.join(iter(read_socket, b''))
    #print(bytes(data))
    #text += data.decode().strip()
    #print(text)
    msg = c.recv(2048).decode()
    msg2 = c.recv(2048).decode()
    print("Connected with", addr)
    try:
       x = re.findall('[0-9]+', msg2)
       finalx = list(filter(imei, x))
       number = finalx[0]
       data = msg.replace(number,'')
       print('IMEI:', number)
       print('TRACKER_DATA:', data)
    except Exception as e:
        print(e)
        print('TRACKER_DATA:', msg2)
    mydb = mysql.connector.connect(
    host="34.234.229.50",
    user="project_user",
    password="Kubernetes@123",
    database="salus"
    )
    print("connection established")
    mycursor = mydb.cursor()
    sql = "INSERT INTO tracker_data (IMEI, TRACKER_DATA) VALUES (%s, %s)"
    val = (number, data)
    mycursor.execute(sql, val)
    mydb.commit()
c.close()















