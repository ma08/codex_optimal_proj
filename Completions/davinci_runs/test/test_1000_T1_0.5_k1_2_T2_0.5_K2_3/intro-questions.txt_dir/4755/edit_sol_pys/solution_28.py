
from sys import stdin

c, k = map(int, stdin.readline().split())

print((c + 10**k - 1) // 10**k * 10**k)
