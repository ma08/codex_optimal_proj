
from math import log10

n, k = map(int, input().split())
print(int(log10(n) / log10(k)) + 1)
