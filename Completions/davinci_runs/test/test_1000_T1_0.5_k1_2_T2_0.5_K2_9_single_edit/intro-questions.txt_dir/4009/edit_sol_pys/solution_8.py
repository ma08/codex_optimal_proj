

n, m = map(int, input().split())
a = list(map(int, input().split()))

if m == 0:
    print(0)
    exit()

a.sort()
b = [0] * n
for i in range(n):
    b[i] = a[i] - a[0]

c = [0] * (b[n-1] + 1)

for i in range(n):
    c[b[i]] += 1

for i in range(1, b[n-1]+1):
    c[i] += c[i-1]

d = [0] * (b[n-1] + 1)

for i in range(n):
    d[b[i]] += 1

for i in range(1, b[n-1]+1):
    d[i] += d[i-1]

e = [0] * (b[n-1] + 1)
for i in range(b[n-1]):
    e[i+1] = e[i] + d[i]

f = [0] * (b[n-1] + 1)
for i in range(b[n-1]):
    f[i+1] = f[i] + c[i]

ans = 10**12
for i in range(1, b[n-1]+1):
    ans = min(ans, e[i] + f[b[n-1]] - f[i])

print(ans)
