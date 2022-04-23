from collections import defaultdict

def solve(n, a, b):
    d = defaultdict(int)
    for i in range(n):
        d[a[i]] += 1
        d[b[i]] += 1
    for i in range(n):
        if d[a[i]] == 1 or d[b[i]] == 1:
            return i + 1
    return -1

n = int(input())
a = []
b = []
for i in range(n):
    a.append(int(input()))
for i in range(n):
    b.append(int(input()))
print(solve(n, a, b))
