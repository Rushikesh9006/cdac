#!/usr/bin/python3
'''
    Dynamic programming --> memoization
'''
result = {0:0, 1:1}

def fibo(num):
    if num not in result:
        result[num] = fibo(num - 1) + fibo(num - 2)
    
    return result[num]

def fiboCaller(num):
    for i in range(num):
        print(f'{i+1} --> {fibo(i)}')

if __name__ == '__main__':

    from sys import argv
    num = int(argv[1]) if len(argv)>1 else 10

    fiboCaller(num)

