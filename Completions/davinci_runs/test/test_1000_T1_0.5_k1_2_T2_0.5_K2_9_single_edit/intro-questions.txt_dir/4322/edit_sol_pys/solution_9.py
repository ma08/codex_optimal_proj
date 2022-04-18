
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
last = None
import math
for h in a:
    if last is None or abs(h - last) <= 1:
        ans.append(h)
        last = h
print(len(ans))
print(' '.join(map(str, ans)))
