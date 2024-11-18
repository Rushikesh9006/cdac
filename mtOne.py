#!/usr/bin/python3

from threading import Thread

def funPrint():
    while True:
        print('X', end='')

if __name__ == '__main__':

    tObj = Thread(target=funPrint)
    tObj.start()
    while True:
        print('O', end='')

    tObj.join()
