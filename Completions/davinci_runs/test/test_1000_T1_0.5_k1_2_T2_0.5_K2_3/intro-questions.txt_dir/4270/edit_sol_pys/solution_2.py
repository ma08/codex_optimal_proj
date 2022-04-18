# -*- coding: utf-8 -*-

import sys, heapq

def main():
    N = int(sys.stdin.readline())
    V = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(V)
    for i in range(N-1):
        x = heapq.heappop(V)
        y = heapq.heappop(V)
        heapq.heappush(V, (x+y)/2)

    print(V[0])

if __name__ == '__main__':
    main()
