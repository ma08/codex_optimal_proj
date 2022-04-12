
n = int(input())  # number of contests
a = [int(x) for x in input().split()]  # the contests

contests = []  # list of contests

for i in range(n):  # loop through all contests
    for j in range(i+1, n):  # loop through contests after i
        if a[j] > a[i] * 2:  # if the contest is too far away, break
            break
        contests.append((a[i], a[j]))  # add the contest

contests.sort()  # sort the contests

max_len = 0  # longest chain of contests
max_contest = None  # the contests in the longest chain

for i in range(len(contests)):  # loop through all contests
    this_contest = [contests[i]]  # the chain of contests we are currently checking
    for j in range(i+1, len(contests)):  # loop through contests after i
        if contests[j][0] > this_contest[-1][1] * 2:  # if the contest is too far away, break
            break
        this_contest.append(contests[j])  # add the contest
    if len(this_contest) > max_len:  # if this chain is longer than the longest chain
        max_len = len(this_contest)  # update the longest chain
        max_contest = this_contest  # update the contests in the longest chain

print(max_len)  # print the longest chain
