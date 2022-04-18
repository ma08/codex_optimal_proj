
from sys import stdin
from math import gcd

t = int(stdin.readline())

for _ in range(t):
    a, b, c, d = map(int, stdin.readline().split())
    g = gcd(gcd(a, b), c)
    print("YES" if d % g == 0 else "NO")
