import sys
sys.setrecursionlimit(10**7)


def main():
    N, M = map(int, input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i], b[i] = map(int, input().split())


if __name__ == '__main__':
    main()
