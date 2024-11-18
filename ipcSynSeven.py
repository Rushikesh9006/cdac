#!/usr/bin/python3

from os import getpid
from time import sleep
from multiprocessing import Process, Value, Semaphore

def funTest(var, sem):
    with sem:#acquire
        for i in range(100):
            var.value += 1
    #released

if __name__ == '__main__':
    var = Value('i', 0)
    sem = Semaphore(1)
    p1 = Process(target=funTest, args = (var,sem))
    print(f'main module here ...{getpid()}') 
    print(f'Before : {var.value}')

    p1.start()
    with sem: # acquiring the lock 
        for i in range(100):
            var.value += 1
    #lock is released here  
    p1.join()
    print(f'After: {var.value}')
    print('-' * 40)
