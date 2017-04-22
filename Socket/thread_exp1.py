import time
from threading import Thread

def Worker(name):
    a = 1
    while flag:
        time.sleep(10)
        print (name, a)

flag = True

burak_thread = Thread(target=Worker, args=('Burak',))
ata_thread = Thread(target=Worker, args=('Ata',))

burak_thread.start()
ata_thread.start()

while True:
    a = input('>>>')   # raw_input
    if a == 'yeter':
        flag = False
        break
