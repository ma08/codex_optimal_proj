

import sys

def solve(n, k, m, scores):
    required_final_score = (n * m) - sum(scores)
    if required_final_score < 0:
        print(-1)
    else:
        print(required_final_score)

if __name__ == '__main__':
    n, k, m = list(map(int, sys.stdin.readline().split()))
    scores = list(map(int, sys.stdin.readline().split()))
    solve(n, k, m, scores)
