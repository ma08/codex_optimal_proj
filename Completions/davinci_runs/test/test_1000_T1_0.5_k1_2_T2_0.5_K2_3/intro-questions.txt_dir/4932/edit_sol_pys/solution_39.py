import sys


def main():
    N, M, K = map(int, sys.stdin.readline().split())
    if N + M >= K and N <= K and M <= K:
        print('Yes')
    else:
        print('No')


main()
