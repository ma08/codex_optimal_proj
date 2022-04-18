
from sys import stdin
from collections import deque

n, c = map(int, stdin.readline().split())  # n = 고양이의 수, c = 사료의 양
weights = deque(map(int, stdin.readline().split()))  # 고양이들의 몸무게

eaten = set()  # 사료를 먹은 고양이들
while weights and c >= weights[0]:
    c -= weights.popleft()
    eaten.add(c)

print(len(eaten))
