

n = int(input())
a = [int(x) for x in input().split()]

contest = []

for i in range(n):
    
    if len(contest) == 0:
        contest.append(a[i])
    elif a[i] <= contest[-1] * 2:
        contest.append(a[i])
    else:
        contest = [a[i]]

print(len(contest))