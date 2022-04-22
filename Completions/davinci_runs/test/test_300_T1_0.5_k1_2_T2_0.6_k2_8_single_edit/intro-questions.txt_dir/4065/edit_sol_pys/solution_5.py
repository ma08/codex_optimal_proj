

n = int(input())
a = [int(x) for x in input().split()]

contests = []

for i in range(n):
    for j in range(i+1, n):
        if a[j] > a[i] * 2:
            break
        contests.append((a[i], a[j]))

contests.sort(key=lambda x: x[1])

max_len = 0
max_contest = None

for i in range(len(contests)):
    this_contest = [contests[i]]
    for j in range(i+1, len(contests)):
        if contests[j][1] > this_contest[-1][0] * 2:
            break
        this_contest.append(contests[j])
    if len(this_contest) > max_len:
        max_len = len(this_contest)
        max_contest = this_contest

print(max_len)
