#!/usr/bin/python3

from threading import Thread

counter = 0

def funPrint():
    global counter
    for _ in range(1000000):
        counter += 1

if __name__ == '__main__':
    from sys import argv
    
    numThreads = int(argv[1]) if len(argv)>1 else 2 
    myThreads = [ Thread(target = funPrint) for _ in range(numThreads)]

    for i in myThreads:
        i.start()

    for _ in range(1000000):
        counter += 1

    for i in myThreads:
        i.join()

    print(f'Finally counter : {counter}')
