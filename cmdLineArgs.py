#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    print(f'Total number of args {len(argv)}')
    print(f'List of args: {argv}')

    print('Printing individual list: ')
    for i in range(len(argv)):
        print(f'argv[{i}] --> {argv[i]}')
