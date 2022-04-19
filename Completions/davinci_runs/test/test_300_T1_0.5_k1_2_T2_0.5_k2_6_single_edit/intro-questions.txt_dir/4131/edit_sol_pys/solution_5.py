from collections import defaultdict


N = int(input())

d = defaultdict(int)
for i in range(N):
    a = int(input())
    d[a] += 1

for key, value in d.items():
    print(str(key) + ' ' + str(value))
