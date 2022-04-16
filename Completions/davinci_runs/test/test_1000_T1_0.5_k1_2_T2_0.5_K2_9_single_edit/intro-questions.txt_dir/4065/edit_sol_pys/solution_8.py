# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 10:01:27 2019
@author: dmatt
"""

n = int(input())
a = [int(x) for x in input().split()]
print(a)
contests = []

for i in range(n):
    for j in range(i+1, n):
        if a[j] > a[i] * 2:
            break
        contests.append((a[i], a[j]))
print(contests)
contests.sort()

max_len = 0
max_contest = None

for i in range(len(contests)):
    this_contest = [contests[i]]
    for j in range(i+1, len(contests)):
        if contests[j][0] > this_contest[-1][1] * 2:
            break
        this_contest.append(contests[j])
    if len(this_contest) > max_len:
        max_len = len(this_contest)
        max_contest = this_contest

print(max_len)
