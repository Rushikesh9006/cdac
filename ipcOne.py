#!/usr/bin/python3

from os import getpid
from time import sleep
from multiprocessing import Process, Queue, current_process

def funTest(que):
    print(f'funTest started... {getpid()}')
    sleep(1)
    que.put(f'Message from {current_process().name}')
    print(f'funTest completed...')
    print('*' * 40)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=funTest, args=(q, ))

    print(f'main module here ...{getpid()}') 
    p1.start()
    msg = q.get()
    print(f'{msg}'.center(40,'*'))
    p1.join()
