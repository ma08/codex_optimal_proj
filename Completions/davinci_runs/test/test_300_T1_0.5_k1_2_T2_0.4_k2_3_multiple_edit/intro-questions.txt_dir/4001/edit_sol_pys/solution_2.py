
import sys
from collections import defaultdict


def main():
    N, M = map(int, input().split())
    d = defaultdict(list)
    for i in range(N):
        d[input()].append(str(i + 1))
    for _ in range(M):
        print(' '.join(d[input()]) or -1)


if __name__ == '__main__':
    main()
