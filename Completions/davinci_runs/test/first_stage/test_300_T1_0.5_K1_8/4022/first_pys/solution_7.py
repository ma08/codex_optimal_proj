

from sys import stdin
from math import inf

if __name__ == '__main__':
    n = int(stdin.readline())
    l = [0] * n
    r = [0] * n
    for i in range(n):
        l[i], r[i] = map(int, stdin.readline().split())

    max_len = 0
    for i in range(n):
        max_len = max(max_len, max(r[i] - l[i], max(r[i] - l[i - 1], r[i - 1] - l[i])))
    print(max_len)