import sys

n, k = [int(i) for i in sys.stdin.readline().split()]

a = [int(i) for i in sys.stdin.readline().split()]

d = dict()
for i in a:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

s = 0
for i in d:
    s += d[i] // 2

print(s)
