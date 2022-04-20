

import sys
import random
import time
import math

class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


def solve(s):
    n = len(s)
    d = [0] * n
    for i in range(n):
        if s[i] == '?':
            d[i] = 3
        else:
            d[i] = 1
    for i in range(1, n):
        d[i] *= d[i - 1]

    res = 0
    for i in range(n - 2):
        if s[i] == 'a' or s[i] == '?':
            for j in range(i + 1, n - 1):
                if s[j] == 'b' or s[j] == '?':
                    for k in range(j + 1, n):
                        if s[k] == 'c' or s[k] == '?':
                            res += d[i] * d[j - i - 1] * d[n - k - 1]
    return res % (10 ** 9 + 7)


def main():
    sys.stdin = open('input.txt')
    n = int(input())
    s = input()
    print(solve(s))


if __name__ == '__main__':
    main()