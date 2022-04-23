

import sys
import math

def main():
    n = int(input()) # number of integers
    a = [int(x) for x in input().split()] # list of integers
    m = int(input()) # number of queries
    for i in range(m):
        l, r, k = [int(x) for x in input().split()]
        print(sum(a[l:r+1]) % k)

if __name__ == '__main__':
    main()
