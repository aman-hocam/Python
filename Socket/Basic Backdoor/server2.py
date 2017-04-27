#-*- coding: UTF-8 -*-
from datetime import datetime
from socket import socket
from threading import Thread

def manage_all(function, args):
    for address in users:
        manage(address, function, args)

def manage(address, function, args):
    command = str({'function': function, 'args': args})
    print ('[{}]: {} << {}'.format(datetime.now(), address, command))

    client = users[address]
    client.sendall(command)

    response = client.recv(1000000)
    print ('[{}]: {} >> {}'.format(datetime.now(), address, response))

def accept():
    client, address = server.accept()
    users[str(address)] = client
    print ('[{}]: {} connected!'.format(datetime.now(), address))

def receptionist():
    while True:
        accept()

users = {}

server = socket()
server.bind(('', 4343))
server.listen(1024)

for i in range(5):
    thread = Thread(target=receptionist)
    thread.start()


# all func *args
# adr func *args

while True:
    try:
        command = raw_input()       # input()

        if command.startswith('all'):
            command = command.split()

            func = command[1]
            args = ' '.join(command[2:])

            manage_all(func, args)

        else:
            command = command.split()

            addr = ' '.join(command[:2])
            func = command[2]
            args = ' '.join(command[3:])

            manage(addr, func, args)

    except:
        print ('Something went wrong!')
