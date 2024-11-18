#!/usr/bin/python3

from threading import Thread, Event
from time import sleep

eventObj = Event()

def funDemo(num):
    print(f'FunDemo with {num} waiting for an event...')
    eventObj.wait()
    print(f'FunDemo with {num} : Continues execution...')


if __name__ =='__main__':
    tObjs = [ Thread(target = funDemo, args=(i+1, )) for i in range(3)]

    for t in tObjs:
        t.start()

    print('Main : sending a signal...')
    sleep(4)
    eventObj.set() #sends signal to  

    for t in tObjs:
        t.join()
    
    print('Main thread completed...')
