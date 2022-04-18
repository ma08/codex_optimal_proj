# -*- coding: utf-8 -*-

import sys, heapq

def main():
    N, M = list(map(int,sys.stdin.readline().split()))
    A = list(map(int,sys.stdin.readline().split()))
    A = [-1 * a for a in A]
    heapq.heapify(A)

    for i in range(M):
        a = heapq.heappop(A)
        heapq.heappush(A, -1 * (-1 * a // 2))

    print(-1 * sum(A))

if __name__ == '__main__':
    main()
