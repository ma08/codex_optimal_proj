

from fractions import gcd

N = int(input())

print(N // gcd(2, N) * 2)