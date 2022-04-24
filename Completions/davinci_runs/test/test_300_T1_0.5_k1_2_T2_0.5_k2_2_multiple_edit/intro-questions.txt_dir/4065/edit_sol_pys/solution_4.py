

n = int(input())
a = [int(x) for x in input().split()]
s = set()
contests = []

for i in range(n):
    for j in range(i+1, n):
        if a[j] > a[i] * 2:  # if the next number is more than twice the current number
            break
        contests.append((a[i], a[j]))

contests.sort()  # sort the contests by the first element

max_len = 0
max_contest = None

for i in range(len(contests)):
    this_contest = [contests[i]]
    for j in range(i+1, len(contests)):
        if contests[j][0] > this_contest[-1][1] * 2:  # if the first element of the next contest is more than twice
            # the second element of the last element of the current contest, stop
            break
        this_contest.append(contests[j])
    if len(this_contest) > max_len:
        max_len = len(this_contest)
        max_contest = this_contest

print(max_len)
