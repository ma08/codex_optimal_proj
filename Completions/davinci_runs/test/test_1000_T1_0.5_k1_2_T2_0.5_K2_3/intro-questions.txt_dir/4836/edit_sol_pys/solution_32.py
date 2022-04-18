

from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
weights = deque(map(int, stdin.readline().split()))  # 큐로 만들기

eaten = set()
while weights and k >= weights[0]:
    c -= weights.popleft()
    eaten.add(k)

print(len(eaten))
