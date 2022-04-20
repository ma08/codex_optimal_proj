

import sys

def solve(n, k, m, scores):
    return max(0, (n * m) - sum(scores))

if __name__ == '__main__':
    n, k, m = list(map(int, sys.stdin.readline().split()))
    scores = list(map(int, sys.stdin.readline().split()))
    print(solve(n, k, m, scores))
