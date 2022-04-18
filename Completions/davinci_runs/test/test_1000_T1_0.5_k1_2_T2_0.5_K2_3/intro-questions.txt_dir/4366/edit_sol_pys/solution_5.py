# -*- coding: utf-8 -*-

import sys

def main():
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print((a+b)%24)

if __name__ == '__main__':
    main()
