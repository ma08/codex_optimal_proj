
import collections
import heapq
import sys

def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    heap = []
    heapq.heapify(heap)
    for i in range(m):
        heapq.heappush(heap, (-a[0] * b[i], 0, i))
    ans = 0
    for i in range(n):
        x = heapq.heappop(heap)
        ans += x[0]
        if x[1] + 1 < m:
            heapq.heappush(heap, (-a[x[1] + 1] * b[x[2]], x[1] + 1, x[2]))
    print(ans)

if __name__ == '__main__':
    main()
