
import math
# Solution

n, m = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * m
for i in a:
    count[i % m] += 1

ans = 0
for i in range(math.ceil(m / 2)):
    if i == 0 or i * 2 == m:
        ans += count[i] % 2
    else:
        ans += max(count[i], count[m - i]) - min(count[i], count[m - i])

print(ans)

for i in range(n):
    print(a[i] + (ans + (a[i] % m) - (n // m) * (a[i] % m)) // 2, end=" ")
