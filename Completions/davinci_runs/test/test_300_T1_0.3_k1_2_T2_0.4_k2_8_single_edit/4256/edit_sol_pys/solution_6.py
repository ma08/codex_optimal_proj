# https://atcoder.jp/contests/abc129/tasks/abc129_a

import sys

if __name__ == '__main__':
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    print(min(B // A, C))
