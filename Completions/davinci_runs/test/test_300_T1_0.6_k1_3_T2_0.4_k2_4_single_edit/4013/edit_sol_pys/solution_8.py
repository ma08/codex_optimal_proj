
from collections import deque
from itertools import combinations

n = int(input())
a = deque(map(int, input().split()))

a = sorted(a)
a = deque(a)

print(min(a[-1] - a[1], a[-2] - a[0]))
