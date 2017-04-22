#-*- coding: UTF-8 -*-
import socket

server = socket.socket(
    family=socket.AF_INET,      # internet ipv4
    type=socket.SOCK_STREAM)

server.connect(('127.0.0.1', 1234))
# server.connect(('104.155.123.11', 1231))

while True:
    message = input('>>> ')   # python2 -> raw_input
    if message == 'exit':
        break
    server.sendall(message.encode('utf-8'))

server.close()
