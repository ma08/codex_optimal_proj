
from math import log

n, k = map(int, input().split())
print(int(log(n)/log(k)) + 1)
