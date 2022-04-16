
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dorm_sums = [0]
for i in range(n):
    dorm_sums.append(dorm_sums[i] + a[i])

for query in b:
    for i in range(n):
        if dorm_sums[i] < query <= dorm_sums[i+1]:
            print(i+1, query - dorm_sums[i])
