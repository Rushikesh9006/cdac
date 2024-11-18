#!/usr/bin/python3

from os import getpid
from time import sleep
from multiprocessing import Process, Pipe, current_process

def funTest(conn):
    print(f'funTest started... {getpid()}')
    sleep(1)
    conn.send(f'Message from {current_process().name}')
    print(f'funTest completed...')
    print('*' * 40)
    conn.close()

if __name__ == '__main__':
    parent, child = Pipe()
    p1 = Process(target=funTest, args=(child, ))

    print(f'main module here ...{getpid()}') 
    p1.start()
    msg = parent.recv()
    print(f'{msg}'.center(40,'*'))

    p1.join()
