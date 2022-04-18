
import sys
import math

def solve(n, m, k, scores):
    required_final_score = (n * m) - sum(scores)
    if required_final_score < 0:
        return -1
    else:
        return required_final_score


if __name__ == '__main__':
    n, m, k = list(map(int, sys.stdin.readline().split()))
    scores = list(map(int, sys.stdin.readline().split()))
    print(solve(n, k, m, scores))
