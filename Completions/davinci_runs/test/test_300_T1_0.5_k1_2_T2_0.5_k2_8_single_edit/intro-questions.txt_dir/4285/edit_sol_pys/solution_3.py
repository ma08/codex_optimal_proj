

#!/usr/bin/env python3

import sys, os

# def main():
#     # read number of chars
#     n = int(sys.stdin.readline())
#     # read chars
#     s = sys.stdin.readline().strip()

#     # count number of a, b, c, ?
#     na = s.count('a')
#     nb = s.count('b')
#     nc = s.count('c')
#     nq = s.count('?')

#     # if there are no ? in s, check if there is a subsequence abc
#     if nq == 0:
#         if 'abc' in s:
#             print(1)
#         else:
#             print(0)
#         return

#     # if there are no a, b, c in s, count number of subsequences abc
#     if na == 0 and nb == 0 and nc == 0:
#         print(3 ** nq)
#         return

#     # prepare a list of possible positions of ?
#     qs = [i for i in range(n) if s[i] == '?']

#     # count number of subsequences abc
#     count = 0

#     for i in range(3 ** nq):
#         # replace ? with a, b, c
#         t = s
#         for j, q in enumerate(qs):
#             t = t[:q] + 'abc'[i // (3 ** (nq - j - 1)) % 3] + t[q + 1:]

#         # count number of subsequences abc
#         if 'abc' in t:
#             count += 1

#     # print result
#     print(count)

# if __name__ == '__main__':
#     main()

# ###############################################################################################################
# ###############################################################################################################
# ###############################################################################################################


# https://atcoder.jp/contests/abc172/tasks/abc172_b

# s = input()
# t = input()

# count = 0
# for i in range(len(s)):
#     if s[i] != t[i]:
#         count += 1

# print(count)


# ###############################################################################################################
# ###############################################################################################################
# ###############################################################################################################


# https://atcoder.jp/contests/abc172/tasks/abc172_c

# n, m, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# sum_a = [0]
# sum_b = [0]
# for i in range(n):
#     sum_a.append(sum_a[i] + a[i])
# for i in range(m):
#     sum_b.append(sum_b[i] + b[i])

# count = 0
# j = m
# for i in range(n + 1):
#     if sum_a[i] > k:
#         break
#     while sum_a[i] + sum_b[j] > k:
#         j -= 1
#     count = max(count, i + j)

# print(count)


# ###############################################################################################################
# ###############################################################################################################
# ###############################################################################################################


# https://atcoder.jp/contests/abc172/tasks/abc172_d

# n = int(input())

# sum = 0
# for i in range(1, n + 1):
#     for j in range(1, int(i ** 0.5) + 1):
#         if i % j == 0:
#             sum += j
#             if i // j != j:
#                 sum += i // j

# print(sum)
