

n = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in range(n):
    if a[i] > a[i-1]:
        ans += a[i] - a[i-1]
    else:
        ans += a[i-1] - a[i]

print(ans)
