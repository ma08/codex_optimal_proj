

from sys import stdin
from heapq import heappop, heappush

def main():
    n, m = [int(i) for i in stdin.readline().split()]
    if m == n-1: # if m is equal to n-1, the total number of operations is the sum of the first m integers
        print(sum(range(1, m+1))
    else:
        heap = [] # create a min heap
        for i in range(n-1, m+1):
            heappush(heap, -(i-n+1) # push the first m integers in the heap
        for i in range(n-1):
            x = -heappop(heap) # pop the smallest element
            heappush(heap, x-1 # push the next smallest element
        print(-sum(heap)

main()
