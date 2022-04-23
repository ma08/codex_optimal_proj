

n, k = map(int, input().split())
a = list(map(int, input().split()[:n]))

for i in range(n):
    if a[i] == 0:
        a[i] = k + 1

ans = 0
for i in range(n):
    ans += a[i] // k
    a[i] %= k

print(best)
