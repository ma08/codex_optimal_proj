

n = int(input())
a = [int(x) for x in input().split()] # a[i] is the number of problems in the ith contest

contests = [] # (a[i], a[j]) is the ith and jth contests

for i in range(n):
    for j in range(i+1, n):
        if a[j] > a[i] * 2:
            break
        contests.append((a[i], a[j])) # add the ith and jth contests

contests.sort() # sort the contests by the number of problems in the first contest

max_len = 0 # max length of the sequence of contests
max_contest = None # max sequence of contests
# for each contest

for i in range(len(contests)):
    this_contest = [contests[i]] # the sequence of contests starting with the ith contest
    # for each contest after the ith contest
    for j in range(i+1, len(contests)):
        if contests[j][0] > this_contest[-1][1] * 2: # if the first contest is too far away
            break
        this_contest.append(contests[j]) # add the contest to the sequence
    if len(this_contest) > max_len:
        max_len = len(this_contest)
        max_contest = this_contest

print(max_len)
