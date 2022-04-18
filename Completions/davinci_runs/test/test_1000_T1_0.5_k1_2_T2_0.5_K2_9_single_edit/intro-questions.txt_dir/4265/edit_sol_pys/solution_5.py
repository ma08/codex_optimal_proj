

n = int(input())
a = list(map(int, input().split()))

ans = float("inf")
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += a[j] * (i + 1) ** (j + 1)
    ans = min(ans, tmp)


print(ans)
