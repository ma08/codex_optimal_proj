# -*- coding: utf-8 -*-

n = int(input())
a = [int(x) for x in input().split()]

contests = []

for i in range(n):
    for j in range(i+1, n):
        if a[j] > a[i] * 2:  # 下一个数字比当前数字的2倍还大，则后面的数字不会满足条件，所以直接退出
            break
        contests.append((a[i], a[j]))

contests.sort()

max_len = 0
max_contest = None

for i in range(len(contests)):
    this_contest = [contests[i]]
    for j in range(i+1, len(contests)):
        if contests[j][0] > this_contest[-1][1] * 2:  # 后面的数字比当前数字的2倍还大，则后面的数字不会满足条件，所以直接退出
            break
        this_contest.append(contests[j])
    if len(this_contest) > max_len:
        max_len = len(this_contest)
        max_contest = this_contest

print(max_len)
