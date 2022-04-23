
n = int(input())  # number of students
a = [int(x) for x in input().split()]  # number of problems solved by each student

contests = []  # list of tuples (a[i], a[j])

for i in range(n):  # for each student
    for j in range(i+1, n):  # for each student after the current one
        if a[j] > a[i] * 2:  # if the second student solved more than twice the problems of the first one
            break
        contests.append((a[i], a[j]))

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
