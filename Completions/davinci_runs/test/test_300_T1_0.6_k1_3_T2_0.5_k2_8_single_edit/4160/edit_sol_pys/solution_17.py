

from collections import deque
n = int(input())
a = deque(map(int, input().split()))
b = deque(map(int, input().split()))
ans = 0
for i in range(n):
    if a[0] > b[0]:
        ans += b[0]
        a[0] -= b[0]
        b.popleft()
    elif a[0] < b[0]:
        ans += a[0]
        b[0] -= a[0]
        a.popleft()
    else:
        ans += a[0]
        a.popleft()
        b.popleft()

print(ans)
