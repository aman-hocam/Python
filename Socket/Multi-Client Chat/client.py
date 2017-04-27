#-*- coding: UTF-8 -*-
from socket import socket
from threading import Thread

def get_messages():
    while True:
        message = server.recv(1024)
        if not message.strip():
            break
        print (message)

server = socket(2, 1)
server.connect(('127.0.0.1', 1231))

while True:
    server.send(raw_input('Username: '))
    status = server.recv(1024)

    if status == '200':
        print ('User created')
        break

    elif status == '500':
        print ('Username already exists!')

thread = Thread(target=get_messages)
thread.start()

while True:
    message = raw_input()
    server.sendall(message)

server.close()
