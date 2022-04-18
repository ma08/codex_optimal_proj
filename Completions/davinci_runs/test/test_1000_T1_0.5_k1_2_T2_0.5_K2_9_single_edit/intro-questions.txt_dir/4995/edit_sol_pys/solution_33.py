

from collections import defaultdict

n = int(input())
d = defaultdict(int)

for _ in range(n):
    s = input()
    d[s] += 1

print(len(d))
for _, v in d.items():
    print(v, end=" ")
