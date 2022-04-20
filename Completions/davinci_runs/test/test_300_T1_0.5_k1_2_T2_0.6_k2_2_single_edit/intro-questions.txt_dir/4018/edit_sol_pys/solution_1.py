#!/usr/bin/python

# -*- coding: utf-8 -*

def main():
    # n, k = map(int, raw_input().split())
    # s = raw_input()
    # # print n, k, s
    # if k > 2**n:
    #     print -1
    # else:
    #     ans = 0
    #     for i in xrange(n):
    #         if k & (1 << i):
    #             ans += n - i
    #     print ans
    a = "abcd"
    if a[0] == a[1]:
        print "yes"
    else:
        print "no"
        
if __name__ == '__main__':
    main()
