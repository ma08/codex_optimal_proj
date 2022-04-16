
from itertools import combinations

n, m = map(int, input().split())

x = list(map(int, input().split()))

x.sort()

for i in range(len(x)):
    if i + m - 1 < len(x):
        print(x[i + m - 1] - x[i], end=' ')
        break
    else:
        print(0, end=' ')
