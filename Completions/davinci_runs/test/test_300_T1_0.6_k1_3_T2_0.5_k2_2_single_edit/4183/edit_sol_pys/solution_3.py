
from fractions import gcd

n = int(input())
t = [int(input()) for _ in range(n)]

ans = t[0]

for i in t:
    ans = ans * i // gcd(ans, i)

print(ans)
