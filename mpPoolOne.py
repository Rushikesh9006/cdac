#!/usr/bin/python3

from time import sleep
from multiprocessing import Pool

def factorial(num):
    sleep(1)
    if num <= 0:
        return 1
    
    return num * factorial(num - 1)

if __name__ == '__main__':

    numbers = [5,6,3,2,-1,9,4]

    with Pool(processes = 5) as pool: # context manager in python
        results = pool.map(factorial, numbers)

    print(f'results : {results}')
