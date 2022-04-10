#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:27:40 2018
@author: joseph
"""

n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(1)
    print('R')
    exit()
# lis_len[i] is the longest increasing subsequence ending before index i
lis_len = [1] * n
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i] and lis_len[j] + 1 > lis_len[i]:
            lis_len[i] = lis_len[j] + 1
# lds_len[i] is the longest decreasing subsequence starting after index i
lds_len = [1] * n
for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if a[j] < a[i] and lds_len[j] + 1 > lds_len[i]:
            lds_len[i] = lds_len[j] + 1
# lcs_len[i] is the longest increasing subsequence ending before index i and
# the longest decreasing subsequence starting after index i
lcs_len = [0] * n
for i in range(n):
    lcs_len[i] = lis_len[i] + lds_len[i] - 1
# the answer is the maximum of the lcs lengths
print(max(lcs_len))
# reconstruct the answer
ans = []
max_len = max(lcs_len)
for i in range(n):
    if lcs_len[i] == max_len:
        # we can start at index i because it is the start of a longest decreasing subsequence
        ans.append(i)
        break
# reconstruct the answer from left to right
for i in range(ans[-1] + 1, n):
    if a[ans[-1]] < a[i] and lis_len[i] + 1 == lis_len[ans[-1]]:
        ans.append(i)
# reconstruct the answer from right to left
for i in range(ans[0] - 1, -1, -1):
    if a[ans[0]] > a[i] and lds_len[i] + 1 == lds_len[ans[0]]:
        ans.insert(0, i)
# output which side was chosen at each step
for i in range(max_len):
    if ans[i] == i:
        print('R', end='')
    else:
        print('L', end='')
print()
