#!/usr/bin/env python

import sys

import heapq # heapq.heapify(list), heapq.heappop(list), heapq.heappush(list, item)

def main():
    num = int(sys.stdin.readline())
    v = list(map(float, sys.stdin.readline().split()))
    heapq.heapify(v)

    for i in range(num-1):
        x = heapq.heappop(v)
        y = heapq.heappop(v)
        heapq.heappush(v, (x+y)/2)

    print(v[0])

if __name__ == '__main__':
    main()
