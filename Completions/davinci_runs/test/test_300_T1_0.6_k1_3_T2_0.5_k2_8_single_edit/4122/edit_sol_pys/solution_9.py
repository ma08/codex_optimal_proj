
import math
import sys

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    return a[-1] - a[0]

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    print(solve())
