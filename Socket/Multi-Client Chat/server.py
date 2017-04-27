#-*- coding: UTF-8 -*-
import time
from socket import socket
from threading import Thread

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def delivery(username):
    count = 0
    while True:
        try:
            message = users[username][0].recv(1024)
        except:
            del users[username]
            break

        if not message.strip():
            count += 1
            continue

        if count > 100:
            del users[username]
            break

        message = '[{}{}{} - {}]: {}{}{}'.format(bcolors.WARNING, username, bcolors.ENDC, time.strftime('%H:%M:%S'), bcolors.OKBLUE, message, bcolors.ENDC)

        for user in users.keys():
            try:
                users[user][0].sendall(message)
            except:
                del users[user]

def accept():
    client, address = server.accept()

    while True:
        username = client.recv(1024)

        if username not in users:
            users[username] = (client, address)
            client.send('200')

            print ('New user: {}'.format(username))
            break

        else:
            client.send('500')

    thread = Thread(target=delivery, args=(username, ))
    thread.start()


def receptionist():
    while True:
        accept()

users = {'': ''}

server = socket()
server.bind(('', 1231))
server.listen(1024)

for i in range(5):
    thread = Thread(target=receptionist)
    thread.start()
