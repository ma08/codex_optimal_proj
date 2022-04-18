#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    n, x, y = map(int, sys.stdin.readline().split())
    num = map(int, sys.stdin.readline().split())
    num = list(num)
    if num[:x+1] == [1] + [0]*x and num[x+1] == 0:
        print 0
        return
    if num[:x+1] == [1] + [1]*x and num[x+1] == 0:
        print 1
        return
    if num[:y+1] == [1] + [0]*y and num[y+1] == 1:
        print 1
        return
    if num[:y+1] == [1] + [1]*y and num[y+1] == 1:
        print 0
        return
    for i in xrange(y+1,x+2):
        if num[i] == 0:
            print 2
            return
    print 1

if __name__ == '__main__':
    main()
