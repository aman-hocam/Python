#-*- coding: UTF-8 -*-
import socket
from threading import Thread

def wait_message(client, address):
    while True:
        message = client.recv(1024).decode('utf-8')
        if message.strip():
            try:
                print (u'[{}]: {}'.format(address, message))
            except:
                pass

def accept():
    while True:
        client, address = server.accept()
        print ('[{}]: connected'.format(address))

        thread = Thread(target=wait_message, args=(client, address))
        thread.start()

server = socket.socket(
    family=socket.AF_INET,      # internet ipv4
    type=socket.SOCK_STREAM)    # TCP
                                # UDP: socket.SOCK_DGRAM
server.bind(('', 1234))
server.listen(1024)

for i in range(5):
    thread = Thread(target=accept)
    thread.start()

# server.close()
