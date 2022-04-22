
import sys


def solve(arr):
    if len(arr) == 1:
        return arr[0]
    heapq.heapify(arr)
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    heapq.heappush(arr, (x+y)/2)
    return solve(arr)

for i in range(num-1):
    x = heapq.heappop(v)
    y = heapq.heappop(v)
    heapq.heappush(v, (x+y)/2)

print(v[0])
