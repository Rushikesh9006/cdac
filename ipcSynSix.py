#!/usr/bin/python3

from os import getpid
from time import sleep
from multiprocessing import Process, Value, Lock

def funTest(var, loc):
    with loc:#acquire
        for i in range(100):
            var.value += 1
    #released

if __name__ == '__main__':
    var = Value('i', 0)
    lock = Lock()
    p1 = Process(target=funTest, args = (var,lock))
    print(f'main module here ...{getpid()}') 
    print(f'Before : {var.value}')

    p1.start()
    with lock: # acquiring the lock 
        for i in range(100):
            var.value += 1
    #lock is released here  
    p1.join()
    print(f'After: {var.value}')
    print('-' * 40)
