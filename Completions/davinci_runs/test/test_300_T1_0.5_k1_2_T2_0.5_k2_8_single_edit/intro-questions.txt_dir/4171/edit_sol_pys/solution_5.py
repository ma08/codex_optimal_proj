
n = int(input())
a = list(map(int, input().split()))[:n]

ans = []
for i in range(n):
    tmp = a[i]
    for j in range(i + 1, n):
        tmp ^= a[j]
    ans.append(tmp)

print(max(ans))
