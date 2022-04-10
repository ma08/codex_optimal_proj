

from sys import stdin
from collections import Counter

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

cnt = Counter(a)

if len(cnt) == 1:
    print(n)
    for i in range(1, n+1):
        print(i, i)
else:
    print(1)
    print(1, n)