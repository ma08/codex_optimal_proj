

n = int(input())
f = [int(x) for x in input().split()]
g = [0] * n

for i in range(n):
    if f[i] == 0:
        g[i] = i + 1
    else:
        g[f[i] - 1] = i + 1

print(' '.join([str(x) for x in g]))
