

import sys, heapq

def main():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))

    # Create a max heap with the heapq module.
    heap = []
    for i in range(N):
        heapq.heappush(heap, -1 * A[i])

    # Pop the first K elements from the heap.
    for i in range(K):
        print(-1 * heapq.heappop(heap))

if __name__ == '__main__':
    main()
