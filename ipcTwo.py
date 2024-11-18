#!/usr/bin/python3

from os import getpid
from time import sleep
from multiprocessing import Process, Queue, current_process

def funTest(que):
    print(f'funTest started... {getpid()}')
    for i in range(5):
        sleep(1)
        que.put(f'Message {i+1} from {current_process().name}')
    print(f'funTest completed...')
    print('*' * 40)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=funTest, args=(q, ))

    print(f'main module here ...{getpid()}') 
    p1.start()
    for _ in range(5):
        msg = q.get()
        print(f'{msg}'.center(40,'*'))
    p1.join()
