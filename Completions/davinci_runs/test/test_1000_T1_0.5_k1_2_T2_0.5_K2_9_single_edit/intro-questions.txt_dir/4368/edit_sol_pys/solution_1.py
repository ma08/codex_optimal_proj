

from math import log

n, k = map(int, input().split())
print(int(log(n, k)) + 1 if n > 1 else 1)
