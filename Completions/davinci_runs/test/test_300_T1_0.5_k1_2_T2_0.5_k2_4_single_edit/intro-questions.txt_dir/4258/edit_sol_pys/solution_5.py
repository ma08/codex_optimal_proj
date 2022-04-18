import sys
sys.setrecursionlimit(1000000)


def main():
    N, K = map(int, input().split())
    print(K - 1 if K != 1 else 0)


if __name__ == '__main__':
    main()
