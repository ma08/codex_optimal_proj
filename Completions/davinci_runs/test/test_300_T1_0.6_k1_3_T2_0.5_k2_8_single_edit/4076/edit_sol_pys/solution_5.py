

import sys
import math 

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[0], A[-1])

if __name__ == '__main__':
    main()
