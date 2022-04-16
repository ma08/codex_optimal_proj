

from sys import stdin
from collections import deque, defaultdict

n, m = map(int, stdin.readline().split())
weights = deque(map(int, stdin.readline().split()))  # weights of each cow
max_cows = defaultdict(int)  # max cows for each weight

for weight in weights:
    for w in max_cows.keys():
        if w + weight <= m:
            max_cows[w + weight] = max(max_cows[w + weight], max_cows[w] + 1)
    max_cows[weight] = max(max_cows[weight], 1)
print(max(max_cows.values()))
