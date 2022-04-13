

import sys
import heapq


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    heapq.heapify(arr)
    for _ in range(m):
        max_value = heapq.heappop(arr)
        heapq.heappush(arr, max_value // 2)
    print(sum(arr))


if __name__ == '__main__':
    main()
