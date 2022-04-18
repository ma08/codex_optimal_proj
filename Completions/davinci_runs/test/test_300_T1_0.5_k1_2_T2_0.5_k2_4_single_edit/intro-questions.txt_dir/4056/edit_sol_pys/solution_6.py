

from collections import deque

n, q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(q)]

n = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in range(1, n):
    ans = lcm(ans, a[i])

print(ans)
