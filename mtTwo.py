#!/usr/bin/python3

from threading import Thread

def funPrint():
    for _ in range(100):
        print('X', end='')

if __name__ == '__main__':

    tObj = Thread(target=funPrint) # 1 
    for _ in range(100):
        print('O', end='')

    tObj.start() #2
    tObj.join() # without using join statement #3
