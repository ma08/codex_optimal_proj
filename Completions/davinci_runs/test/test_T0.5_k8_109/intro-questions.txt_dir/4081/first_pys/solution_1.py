

from collections import deque

n = int(input())
a = list(map(int, input().split()))

l = deque()
r = deque()

for i in range(n):
    l.append(a[i])
    r.appendleft(a[n-i-1])

ans = []
while len(l) > 0:
    if l[0] < r[0]:
        ans.append('L')
        l.popleft()
    else:
        ans.append('R')
        r.popleft()

print(len(ans))
print(''.join(ans))