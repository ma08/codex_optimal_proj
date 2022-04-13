

n, m = map(int, input().split())  # number of dorms, number of queries
a = list(map(int, input().split()))  # number of students in each dorm
b = list(map(int, input().split()))  # number of students in the dorm

dorm_sums = [0]  # number of students in the dorm
for i in range(n):
    dorm_sums.append(dorm_sums[i] + a[i])  # number of students in the dorm

for query in b:  # number of students in each dorm
    for i in range(1, n+1):
        if dorm_sums[i] >= query:  # number of students in each dorm
            print(i, query - dorm_sums[i-1])  # number of students in the dorm
            break
