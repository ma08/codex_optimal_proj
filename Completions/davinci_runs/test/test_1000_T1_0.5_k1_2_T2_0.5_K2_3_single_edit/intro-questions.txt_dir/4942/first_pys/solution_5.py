

import sys
import heapq

def main():
    n = int(sys.stdin.readline())
    days = map(int, sys.stdin.readline().split())
    heap = []
    for i in days:
        heapq.heappush(heap, i)
    time = 0
    while heap:
        time += heapq.heappop(heap)
        if heap:
            time += 1
    print time

if __name__ == "__main__":
    main()