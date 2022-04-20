

import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

likes = defaultdict(int)

for _ in range(N):
    K = list(map(int, sys.stdin.readline().split()))
    for k in K[1:]:
        likes[k] += 1

print(len([l for l in likes if likes[l] == N]))