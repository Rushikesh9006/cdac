#!/usr/bin/python3

from threading import Thread, RLock
counter = 0 # global shared data
lock = RLock() #globally creating RLock object

def funPrint():
    global counter
    lock.acquire()
    try:
        for _ in range(1000000):
            counter += 1
    finally:
        lock.release()

if __name__ == '__main__':
    from sys import argv
    
    numThreads = int(argv[1]) if len(argv)>1 else 2 
    myThreads = [ Thread(target = funPrint) for _ in range(numThreads)]

    for i in myThreads:
        i.start()

    lock.acquire()
    try:
        for _ in range(1000000):
            counter += 1
    finally:
        lock.release()

    for i in myThreads:
        i.join()
    print(f'Finally counter : {counter}')
