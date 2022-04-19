n = int(input())
a = list(map(int, input().split()))


contest = []

for i in range(n):
    for j in range(i+1, n):
        if a[j] > a[i] * 2:
            break
        contest.append((a[i], a[j]))

contest.sort()

max_len = 0
max_contest = []

    this_contest = [contest[i]]
    for j in range(i+1, len(contest)):
        if contest[j][0] > this_contest[-1][1] * 2:
            break
        this_contest.append(contest[j])
    if len(this_contest) > max_len:
        max_len = len(this_contest)
        max_contest = this_contest

print(max_len)
