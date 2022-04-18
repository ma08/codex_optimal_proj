
from sys import stdin

c, k = map(int, stdin.readline().split()) # k: 기준

print((c + 10**k - 1) // 10**k * 10**k) # 10**k: 기준
