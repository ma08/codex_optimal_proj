

import sys
import bisect


def main():
    n = int(sys.stdin.readline())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    lst.sort()
    max_val = float('-inf')
    for i in range(n):
        if i == 0:
            max_val = max(max_val, lst[i] * sum(lst[i + 1:]))
        elif i == n - 1:
            max_val = max(max_val, lst[i] * sum(lst[:i]))
        else:
            max_val = max(max_val, lst[i] * sum(lst[:i]) + lst[i] * sum(lst[i + 1:]))
    print(max_val)


if __name__ == '__main__':
    main()
