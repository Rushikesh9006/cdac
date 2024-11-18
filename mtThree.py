#!/usr/bin/python3

from threading import Thread

counter = 0

def funPrint():
    global counter
    for _ in range(1000000):
        counter += 1

if __name__ == '__main__':

    tObj1 = Thread(target=funPrint) # 1 
    tObj2 = Thread(target=funPrint) # 1 

    for _ in range(1000000):
        counter += 1

    tObj1.start() #2
    tObj2.start() #2


    tObj1.join() # without using join statement #3
    tObj2.join() # without using join statement #3

    print(f'Finally counter : {counter}')
