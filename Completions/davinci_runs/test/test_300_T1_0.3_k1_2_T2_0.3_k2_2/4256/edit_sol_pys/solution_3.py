
import sys

if __name__ == '__main__':
    N, A, B = map(int, sys.stdin.readline().rstrip().split())
    print(min(N * A, B))
