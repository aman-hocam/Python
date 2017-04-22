#-*- coding: UTF-8 -*-
import time, random
from threading import Thread

#import urllib
#import urlparse

def Work(name):
    print ("Worker {} started now".format(name))
    wait = random.randint(1, 10)
    time.sleep(wait)
    print ("Worker {} finished at {}!".format(name, wait))


for i in range(3):
    thread = Thread(target=Work, args=(i+1,))
    thread.start()
    # Work(i+1)
