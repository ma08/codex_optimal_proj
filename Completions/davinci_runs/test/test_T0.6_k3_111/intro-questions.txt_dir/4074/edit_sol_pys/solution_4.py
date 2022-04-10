
# test1
from math import ceil

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(ceil(n/k))
