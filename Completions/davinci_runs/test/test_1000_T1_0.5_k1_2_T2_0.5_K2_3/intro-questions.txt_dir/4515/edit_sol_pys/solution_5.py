

from sys import stdin
from math import gcd
t = int(stdin.readline())

for _ in range(t):
    a, b, c, n = map(int, stdin.readline().split())
    d = gcd(gcd(a, b), c)
    print("YES" if n % d == 0 else "NO")
