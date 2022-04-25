

n = int(input())
a = [int(x) for x in input().split()]
contests = []

for i in range(n):
    for j in range(i+1, n):
        if a[j] > a[i] * 2:
            break
        contests.append((i, j))

contests.sort()

max_len = 0
max_contest = None

for i in range(len(contests)):
    this_contest = [contests[i]]
    for j in range(i+1, len(contests)):
        if a[contests[j][0]] > a[this_contest[-1][1]] * 2 or contests[j][0] <= this_contest[-1][1]:
            break
        this_contest.append(contests[j])
    if len(this_contest) > max_len:
        max_len = len(this_contest)
        max_contest = this_contest

print(max_len)
