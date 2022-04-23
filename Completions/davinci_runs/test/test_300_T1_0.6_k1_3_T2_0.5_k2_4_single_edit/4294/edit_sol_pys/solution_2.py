

import sys
input = sys.stdin.readline

x, a = map(int, input().rstrip().split())

if x < a:
    print(0)
else:
    print(10)
