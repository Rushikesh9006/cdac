#!/usr/bin/python3

def fibo(num):
    if num <= 1:
        return num

    return fibo(num - 1) + fibo(num - 2)


def fiboCaller(num):
    for i in range(num):
        print(f'{i+1} --> {fibo(i)}')



if __name__ == '__main__':

    from sys import argv
    num = int(argv[1]) if len(argv)>1 else 10

    fiboCaller(num)

