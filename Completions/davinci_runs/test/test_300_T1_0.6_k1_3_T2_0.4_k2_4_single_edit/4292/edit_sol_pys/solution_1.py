
import sys

def solution(N, K):
    prices = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    total = 0
    for i in range(K):
        total += prices[i]
    print(total)
    
if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    solution(N, K)
