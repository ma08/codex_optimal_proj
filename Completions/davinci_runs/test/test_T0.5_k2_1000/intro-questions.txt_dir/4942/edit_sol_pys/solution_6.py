

import sys
import heapq

def main():
    n = int(sys.stdin.readline())
    days = list(map(int, sys.stdin.readline().split())) # read the line and split it into a list of integers
    heap = []
    for i in days:
        heapq.heappush(heap, i) # push the integers into the heap
    time = 0
    while heap:
        time += heapq.heappop(heap)
        if heap:
            time += 1
    print(time)

if __name__ == "__main__":
    main()
