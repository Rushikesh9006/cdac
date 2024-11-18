#!/usr/bin/python3

from threading import Thread, Event
from time import sleep

eventObj = Event()

def funDemo():
    print('FunDemo waiting for an event...')
    eventObj.wait()
    print('FunDemo : Continues execution...')


if __name__ =='__main__':
    tObj = Thread(target = funDemo)

    tObj.start()

    print('Main : sending a signal...')
    sleep(4)
    eventObj.set() #sends signal to  

    tObj.join()
    print('Main thread completed...')
