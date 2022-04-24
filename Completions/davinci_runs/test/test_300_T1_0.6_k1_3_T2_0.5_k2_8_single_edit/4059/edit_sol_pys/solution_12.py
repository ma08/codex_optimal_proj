from collections import Counter
from collections import defaultdict
import sys


sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


for a in range(1, N):
    b = (N - a) // 2
    if 2 * a + 2 * b == N:
        ans += 3
    elif 2 * a + 2 * b + 1 == N:
        ans += 4

print(ans)
