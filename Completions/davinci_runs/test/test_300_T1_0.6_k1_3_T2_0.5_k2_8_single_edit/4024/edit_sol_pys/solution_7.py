
import sys
from collections import defaultdict


def min_cost(n, k, s):
    cost = 0
    while k > 0:
        if k > len(s):
            return -1
        if k == 1:
            return cost + len(s)
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        max_count = max(counts.values())
        cost += (len(s) - max_count)
        s = s[:max_count]
        k -= 1
    return cost

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())
    s = sys.stdin.readline().strip()
    print(min_cost(n, k, s))
