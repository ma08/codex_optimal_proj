#!/usr/bin/env python3

import sys
import heapq

num = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))

if num == 1:
    print(v[0])
    exit()

heapq.heapify(v)

for i in range(num-1):
    x = heapq.heappop(v)
    y = heapq.heappop(v)
    heapq.heappush(v, (x+y)/2)

print(v[0])
