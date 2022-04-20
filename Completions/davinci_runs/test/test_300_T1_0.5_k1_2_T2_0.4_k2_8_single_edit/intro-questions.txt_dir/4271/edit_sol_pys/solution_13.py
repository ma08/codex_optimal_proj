

from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

q = deque(a)
ans = 0
while m > 0:
    ans += q.pop()
    m -= 1
    q.appendleft(q.pop())

print(ans) 
