#!/usr/bin/python3

from os import getpid
from time import sleep
from multiprocessing import Process

def funTest():
    print(f'funTest started... {getpid()}')
    sleep(1)
    print(f'funTest completed...')
    print('*' * 40)


if __name__ == '__main__':
    from sys import argv    
    procList = []
    
    num = int(argv[1]) if len(argv) > 1 else 5

    print(f'main module here ...{getpid()}') 
    for i in range(num):
        p = Process(target=funTest)
        procList.append(p)
        p.start()

    for i in procList:
        i.join()

    print('-' * 40)
