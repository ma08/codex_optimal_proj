#!/usr/bin/env python3

def main():
    Y, P = input().strip().split()
    if Y[-1] == 'e' and Y[-2] not in 'aiou':
        print('{}x{}'.format(Y, P))
    elif Y[-1] in 'aiou' and Y[-2] not in 'aiou':
        print('{}ex{}'.format(Y[:-1], P))
    elif Y[-1] in 'aiou' and Y[-2] in 'aiou':
        print('{}ex{}'.format(Y, P))
    else:
        print('{}ex{}'.format(Y, P))

main()
