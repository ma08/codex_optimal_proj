

import sys


def get_nums():
    return map(int, sys.stdin.readline().strip().split())


b, k, g = get_nums()

print(b, k, g)
