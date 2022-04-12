
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dorm_sum = [0]
for i in range(n):
    dorm_sum.append(dorm_sum[i] + a[i])

for query in b:
    for i in range(1, n+1):
        if dorm_sum[i] >= query:
            print(i, query - dorm_sum[i-1])
            break
