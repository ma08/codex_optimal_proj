

import sys

# a, b, c, d = map(int, sys.stdin.readline().split())
# print(max(a*c, a*d, b*c, b*d))

a, b, c, d = map(int, sys.stdin.readline().split())
print(max(a*c, a*d, b*c, b*d))

"""
int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a = [int(sys.stdin.readline()) for _ in range(N)]
a = sys.stdin.readline().rstrip()
"""