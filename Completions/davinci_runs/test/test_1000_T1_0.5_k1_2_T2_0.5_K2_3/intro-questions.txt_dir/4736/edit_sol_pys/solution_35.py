
# n, k = map(int, input().split())
# a = [int(i) for i in input().split()]

# def fact(n):
#     ans = 1
#     for i in range(1, n+1):
#         ans *= i
#     return ans

# def ncr(n, r):
#     return int(fact(n)/(fact(r)*fact(n-r)))

# if k == 1:
#     print(sum(a))
# else:
#     ans = 0
#     for i in range(1, k+1):
#         ans += a[i-1]*ncr(sum(a[i:]), k-i)
#     print(ans)

import sys
import math

# input = sys.stdin.readline
n, k = map(int, input().split())
r = [int(input()) for _ in range(n)]
r.sort()
r = r[::-1]

def calc(x):
    return x*(x+1)//2

ans = 0
for i in range(k):
    ans += r[i]*calc(i)
    ans -= r[i]*calc(n-i-1)
print(ans)
