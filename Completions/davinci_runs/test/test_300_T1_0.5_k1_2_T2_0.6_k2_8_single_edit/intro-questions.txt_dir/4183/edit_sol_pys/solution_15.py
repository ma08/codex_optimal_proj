# -*- coding:utf-8 -*-
import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd_list(A):
    if len(A) == 1:
        return A[0]
    else:
        return gcd(A[0], gcd_list(A[1:]))


def lcm_list(A):
    if len(A) == 1:
        return A[0]
    else:
        return lcm(A[0], lcm_list(A[1:]))


def gcd_list2(A):
    ans = A[0]
    for a in A[1:]:
        ans = gcd(ans, a)
    return a


def lcm_list2(A):
    ans = A[0]
    for a in A[1:]:
        ans = lcm(ans, a)
    return ans


def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = 1
    for t in T:
        ans = lcm(ans, t)
    print(ans)

if __name__ == '__main__':
    main()
