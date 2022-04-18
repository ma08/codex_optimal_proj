
import sys

def solve(N, K, H):
    H.sort()
    return 0 if K >= N else sum(H[K:])

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().rstrip().split())
    H = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solve(N, K, H))
