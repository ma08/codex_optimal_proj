from operator import itemgetter

from collections import Counter

N = int(input())
ab = []
for i in range(N):
    a, b = map(int, input().split())
    ab.append([a, b])

ab.sort(key=itemgetter(1), reverse=True)

ans = 0
for i in range(N):
    a, b = ab[i]
    if i % 2 == 0:
        ans += a
    else:
        ans -= a

print(ans)
