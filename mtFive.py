#!/usr/bin/python3

from threading import Thread, Lock
counter = 0 # global shared data
lock = Lock() #globally creating Lock object

def funPrint():
    global counter
    with lock:
        for _ in range(1000000):
            counter += 1

if __name__ == '__main__':
    from sys import argv
    
    numThreads = int(argv[1]) if len(argv)>1 else 2 
    myThreads = [ Thread(target = funPrint) for _ in range(numThreads)]

    for i in myThreads:
        i.start()

    with lock:
        for _ in range(1000000):
            counter += 1

    for i in myThreads:
        i.join()
    print(f'Finally counter : {counter}')
