

import sys
import math


def solution(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return -1
            else:
                return 0
        else:
            return 1
    else:
        delta = b * b - 4 * a * c
        if delta < 0:
            return 0
        else:
            if delta == 0:
                return 1
            else:
                return 2


if __name__ == "__main__":
    # n = int(input())
    # a = list(map(int, input().split()))
    # a.sort()
    # for i in a:
    #     print(i, end=' ')
    a = int(input())
    b = int(input())
    c = int(input())
    print(solution(a, b, c))
