# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque


def main():
    n, k = map(int, input().split())
    problems = list(map(int, input().split()))
    ans = 0
    while problems:
        if problems[0] <= k:
            ans += 1
            problems.pop(0)
        elif problems[-1] <= k:
            ans += 1
            problems.pop(-1)
        else:
            break
    print(ans)


if __name__ == '__main__':
    main()
