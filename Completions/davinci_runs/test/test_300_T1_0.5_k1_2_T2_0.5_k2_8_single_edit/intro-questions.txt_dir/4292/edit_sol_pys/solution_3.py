
import sys, heapq
input = sys.stdin.readline
n, k = map(int, input().split())
p = list(map(int, input().split()))
heapq.heapify(p)
ans = 0
for i in range(k):
    ans += heapq.heappop(p)
print(ans)
