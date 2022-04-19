
import sys

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

min_lcm = 10**7 + 1
min_i = 0
min_j = 0

for i in range(n):
    for j in range(i + 1, n):
        if lcm(a[i], a[j]) < min_lcm:
            min_lcm = lcm(a[i], a[j])
            min_i = i
            min_j = j

print(min_i + 1, min_j + 1)
