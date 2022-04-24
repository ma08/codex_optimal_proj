
n, m, k = map(int, input().split())

a = list(map(int, input().split()))

res = [0] * n

for i in range(n):
    for j in range(n):
        if abs(a[i] - a[j]) > k:
            res[i] += 1

print(*res)
