
import sys
# Solution

n, m = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * m
for i in a:
    count[i % m] += 1

ans = 0
for i in range(m // 2 + 1):
    if i == 0 or i * 2 == m:
        ans += count[i] % 2
    else:
        ans += max(count[i], count[m - i]) - min(count[i], count[m - i])

sys.stdout.write(str(ans)+'\n')

for i in range(n):
    sys.stdout.write(str(a[i] + (ans + (a[i] % m) - (n // m) * (a[i] % m)) // 2)+' ')
