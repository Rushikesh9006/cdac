#!/usr/bin/python3

from os import getpid
from time import sleep
from multiprocessing import Process

def funTest(args):
    print(f'funTest started... {getpid()} with Job id: {args[0]}')
    sleep(args[1])
    print(f'funTest completed...')
    print('*' * 40)


if __name__ == '__main__':
    
    procList = []
    argList = [(1,3),(2,2), (3, 2)]

    print(f'main module here ...{getpid()}') 
    for i in range(3):
        p = Process(target=funTest, args=(argList[i], ))
        procList.append(p)
        p.start()

    for i in procList:
        i.join()

    print('-' * 40)
