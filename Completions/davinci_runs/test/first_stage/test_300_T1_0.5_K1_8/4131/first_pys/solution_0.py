

import sys


def main():
    n, m = map(int, input().split())
    prefectures = [[] for _ in range(n+1)]
    for _ in range(m):
        p, y = map(int, input().split())
        prefectures[p].append(y)
    for p in range(1, n+1):
        prefectures[p].sort()
        for i, year in enumerate(prefectures[p]):
            print('{:0>6}{:0>6}'.format(p, i+1))


if __name__ == '__main__':
    main()