#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Juan Gallostra, jgallostra<at>bonadrone.com
# Date: 12-18-2018

'''
    File description: 
'''


import sys


def main():
    '''
        Main function
    '''
    n = int(sys.stdin.readline())
    num = n
    while True:
        if num % 2 == 0:
            print(num)
            break
        num += n


if __name__ == '__main__':
    main()
