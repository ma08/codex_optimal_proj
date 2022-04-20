

from math import gcd

N = int(input())
T = [int(input()) for _ in range(N)]

print(int(T[0] * T[1] / gcd(T[0], T[1])))