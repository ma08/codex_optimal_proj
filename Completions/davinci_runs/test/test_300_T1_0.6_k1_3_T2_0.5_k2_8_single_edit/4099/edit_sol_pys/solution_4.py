
import sys

def solve(n, k, m, scores, total_score):
    required_final_score = (n * m) - total_score
    if required_final_score < 0: return -1
    if required_final_score > k: return -1
    return required_final_score

if __name__ == '__main__':
    n, k, m = list(map(int, sys.stdin.readline().split()))
    scores = list(map(int, sys.stdin.readline().split()))
    print(solve(n, k, m, scores))
