

import sys

# n = int(input())
# a = list(map(int, input().split()))
# a = [int(input()) for _ in range(n)]
# s = input()
# s = input().rstrip().split(' ')
# n = int(sys.stdin.readline())
n, k = map(int, sys.stdin.readline().split())

if n % k == 0:
    ans = 0
else:
    ans = 1
print(ans)