
# Solution

n, w = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

x = [0] * n

for i in range(n):
    x[i] = x[i - 1] + a[i]

x.sort()

ans = 0

for i in range(n):
    if x[i] - x[i - 1] >= 0:
        ans += x[i] - x[i - 1] + 1

print(min(ans, w + 1))
