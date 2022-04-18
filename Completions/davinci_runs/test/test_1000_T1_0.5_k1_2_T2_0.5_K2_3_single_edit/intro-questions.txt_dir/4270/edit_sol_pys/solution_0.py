

import sys
import heapq

num = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))
heapq.heapify(v) # 최소 힙

for i in range(num-1):
    x = heapq.heappop(v)
    y = heapq.heappop(v)
    heapq.heappush(v, (x+y)/2) # 현재 최소값과 두번째 최소값을 평균내서 최소 힙에 넣는다.

print(v[0])
