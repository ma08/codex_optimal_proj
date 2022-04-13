#!/usr/bin/python

import sys

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print('YES' if b-a == c-b else 'NO')

if __name__ == '__main__':
    main()
