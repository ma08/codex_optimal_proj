

from collections import deque, defaultdict

n = int(input())
d = defaultdict(list)

for i in range(n):
    s = input()
    d[len(s)].append(s)

for k in sorted(d.keys()):
    for i in sorted(d[k]):
        print(i)
