
import sys

sys.setrecursionlimit(10**6)

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N, K = map(int, sys.stdin.readline().strip().split())
        print(N, K)

if __name__ == "__main__":
    main()
