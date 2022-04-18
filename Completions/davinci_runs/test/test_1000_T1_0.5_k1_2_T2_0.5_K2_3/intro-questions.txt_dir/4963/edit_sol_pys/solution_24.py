from collections import deque

n = int(input())
d = deque(map(int, input().split()))

ans = []

for i in range(n):
    if d[0] == i + 1:
        d.popleft()
    else:
        ans.append(d.pop())

print(' '.join(map(str, ans)))
