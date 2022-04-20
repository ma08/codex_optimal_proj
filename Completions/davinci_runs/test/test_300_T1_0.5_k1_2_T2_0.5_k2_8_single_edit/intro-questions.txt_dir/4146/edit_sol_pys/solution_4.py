

from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
c = sorted(c.items(), key=lambda x: x[1], reverse=True)

if len(c) == 1:
    print(c[0][1])
elif c[0][1] > c[1][1]:
    print(N - c[0][1])
else:
    print(N - (c[0][1] + c[1][1]))
