

n = int(input()) + 1
a = [int(x) for x in input().split()] + [0]

contests = []

for i in range(n - 1):
    for j in range(i+1, n - 1):
        if a[j] > a[i] * 2:
            break
        contests.append((a[i], a[j]))

contests.sort(key=lambda x: (x[0], x[1]))

print(contests)

max_len = 0
max_contest = None

for i in range(len(contests)):
    this_contest = [contests[i]]
    for j in range(i+1, len(contests)):
        if contests[j][0] > this_contest[-1][1] * 2 or contests[j][1] < this_contest[-1][0] * 2:
            break
        this_contest.append(contests[j])
    if len(this_contest) > max_len:
        max_len = len(this_contest)
        max_contest = this_contest

print(max_len)
print(max_contest)
