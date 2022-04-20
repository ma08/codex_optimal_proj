

# https://atcoder.jp/contests/abc065/tasks/arc076_a

import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
A, B = map(int, input().rstrip().split())

if M == 1:
    print(0)
    sys.exit()

if A > B:
    print(0)
    sys.exit()

print(total)
