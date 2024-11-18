#!/usr/bin/python3

from os import getpid
from time import sleep
from multiprocessing import Process

def funTest(args):
    print(f'funTest started... {getpid()} with {args}')
    sleep(1)
    print(f'funTest completed...')
    print('*' * 40)

if __name__ == '__main__':

    p1 = Process(target=funTest, args=('One argument here', ))
    print(f'main module here ...{getpid()}') 
    p1.start()
    print('-' * 40)
    p1.join()
