#!/usr/bin/python3
import sys
from collections import deque


def main():
    input = sys.stdin.readline
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0] * N
    que = deque()
    for i in range(N):
        que.append(i)
    for a in A:
        B[que.popleft()] = a
    for b in B:
        print(b, end=' ')

if __name__ == '__main__':
    main()
