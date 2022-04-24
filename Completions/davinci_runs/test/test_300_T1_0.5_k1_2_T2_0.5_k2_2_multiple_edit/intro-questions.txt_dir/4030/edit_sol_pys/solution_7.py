
import sys

n = int(input())
s = input()

if n == 1:
    print(1)
    print(1)
    sys.exit()

if n == 2:
    print(1)
    print(1, 1)
    sys.exit()

c = [1] * n

for i in range(1, n):
    if s[i] > s[i - 1]:
        c[i] = max(c[i], c[i - 1])
        c[i - 1] = max(c[i], c[i - 1])

for i in range(n - 1, 0, -1):
    if s[i] < s[i - 1]:
        c[i] = max(c[i], c[i - 1])
        c[i - 1] = max(c[i], c[i - 1])

print(max(c))
print(*c)
