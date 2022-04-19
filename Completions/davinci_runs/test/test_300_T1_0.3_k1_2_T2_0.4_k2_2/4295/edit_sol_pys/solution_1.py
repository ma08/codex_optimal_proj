
import sys
sys.setrecursionlimit(10**6)
# N, K = map(int, input().split())
N, K = 7, 4


def main():
    if N % K == 0:
        print(0)
    else:
        print(min(N % K, K - N % K))


if __name__ == "__main__":
    main()
