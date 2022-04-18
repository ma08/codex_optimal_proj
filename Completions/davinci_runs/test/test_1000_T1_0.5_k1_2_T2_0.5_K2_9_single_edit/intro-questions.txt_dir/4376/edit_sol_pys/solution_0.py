
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dorm_sums = [0]
for i in range(n):
    dorm_sums.append(dorm_sums[i] + a[i])

for i in range(m):
    for j in range(1, n+1):
        if dorm_sums[j] >= b[i]:
            print(j, b[i] - dorm_sums[j-1])
            break
