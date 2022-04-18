# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque


def main():
    a, p = map(int, input().split())
    print(p // 2 + (a + p % 2) * 3 // 2)


if __name__ == '__main__':
    main()
