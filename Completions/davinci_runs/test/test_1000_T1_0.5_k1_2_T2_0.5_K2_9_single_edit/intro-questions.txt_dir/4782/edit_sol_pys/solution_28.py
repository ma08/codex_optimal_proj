
from sys import stdin
from heapq import heappop, heappush

def main():
    n, m = [int(i) for i in stdin.readline().split()]
    heap = []
    for i in range(n-1, m+1):
        heappush(heap, -(i-n+1))
    for i in range(n-1):
        x = -heappop(heap)
        heappush(heap, x-1)
    print(-sum(heap))

main()
