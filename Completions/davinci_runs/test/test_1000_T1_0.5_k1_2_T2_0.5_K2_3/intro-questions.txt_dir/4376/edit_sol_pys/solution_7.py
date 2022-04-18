

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dorm_dict = {}
dorm_sums = [0]
for i in range(n):
    dorm_sums.append(dorm_sums[i] + a[i])

for i in range(1, n+1):
    dorm_dict[dorm_sums[i]] = i

for query in b:  # for each query
    for i in range(1, n+1):  # for each dorm
        if dorm_sums[i] >= query:  # if the dorm sum is greater than or equal to the query
            print(i, query - dorm_sums[i-1])  # print the dorm and the student number




            break
