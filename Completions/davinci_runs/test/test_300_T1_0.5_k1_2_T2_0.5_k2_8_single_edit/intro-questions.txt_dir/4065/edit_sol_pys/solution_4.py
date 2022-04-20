

n = int(input())  # number of contests
a = [int(x) for x in input().split()]  # difficulty of each contest

contests = []
# O(n^2)

for i in range(n):
    for j in range(i+1, n):
        if a[j] > a[i] * 2:
            break
        contests.append((a[i], a[j]))
# O(nlogn)

contests.sort()

max_len = 0  # max number of contests
max_contest = None  # max contest
# O(n^2)

for i in range(len(contests)):
    this_contest = [contests[i]]
    for j in range(i+1, len(contests)):
        # if the current contest is not hard enough to be a part of the current streak
        if contests[j][0] > this_contest[-1][1] * 2:
            break
        # add the contest to the current streak
        this_contest.append(contests[j])
    # if the current streak is the longest
    if len(this_contest) > max_len:
        # update the max
        max_len = len(this_contest)
        max_contest = this_contest

print(max_len)
