#!/usr/bin/python3

from os import getpid
from time import sleep
from multiprocessing import Process, Array

def funTest(myArray):
    for i in range(len(myArray)):
        sleep(1)
        myArray[i] +=  101 + i;


if __name__ == '__main__':
    someArray = Array('i', [0,0,0,0,0,0])
    p1 = Process(target=funTest, args = (someArray,))
    print(f'main module here ...{getpid()}') 
    print(f'Before Array: {list(someArray)}')
    p1.start()
    p1.join()
    print(f'After Array: {list(someArray)}')
    print('-' * 40)
