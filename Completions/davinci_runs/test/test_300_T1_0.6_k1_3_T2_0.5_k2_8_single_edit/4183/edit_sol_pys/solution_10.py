
from fractions import gcd
import sys

n = int(input())
t = []
for i in range(n):
    t.append(int(input()))

ans = t[0]

for i in t:
    ans = ans * i // gcd(ans, i) # gcd = greatest common divisor

print(ans)
