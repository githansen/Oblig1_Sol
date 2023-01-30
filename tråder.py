from threading import Thread
import socket 
import select 
import time

def tråd1():
    while True:
        print("tråd 1 kjører")
        time.sleep(2)


def tråd2():
    while True:
        print("Tråd 2 kjører")
        time.sleep(2)


t1 = Thread(target=tråd1)
t2 = Thread(target=tråd2)
t1.start()
t2.start()