

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

f = [0] * h

for i in range(n):
    for j in range(h):
        f[j] = max(f[j], f[(j - a[i] + 1) % h])
    for j in range(l, r + 1):
        f[j] += 1

print(max(f))