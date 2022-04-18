

from sys import stdin
from collections import deque

n, c = map(int, stdin.readline().strip().split())
weights = deque(map(int, stdin.readline().strip().split()))

eaten = set()
while weights and c >= weights[0]:
    c -= weights.popleft()
    eaten.add(c)

print(len(eaten))
