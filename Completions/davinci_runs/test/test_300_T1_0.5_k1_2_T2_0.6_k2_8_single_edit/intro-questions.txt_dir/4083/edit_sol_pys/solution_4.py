from collections import defaultdict

n, k = [int(i) for i in input().split()]
d = defaultdict(int)
a = [int(i) for i in input().split()]

for i in a:
    d[i] += 1

print(len(d.keys()))
