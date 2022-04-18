import sys


n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

g = [0]

for i in range(n):
    if a[i] > g[-1]:
        g.append(a[i])
    else:
        for j in range(len(g)):
            if a[i] <= g[j]:
                g[j] = a[i]
                break

print(len(g))
print(*g)
