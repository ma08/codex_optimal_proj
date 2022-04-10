

from sys import stdin
from math import gcd

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

result = [1, 2]
min_lcm = a[0] * a[1] // gcd(a[0], a[1])

for i in range(n):
    for j in range(i + 1, n):
        lcm = a[i] * a[j] // gcd(a[i], a[j])
        if lcm < min_lcm:
            min_lcm = lcm
            result = [i + 1, j + 1]

print(*result)