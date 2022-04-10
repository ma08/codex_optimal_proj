

n = int(input())
a = list(map(int, input().split()))

m = 0
ans = 0
for i in range(n):
    m += a[i]
    if m == 0:
        ans += 1
        m = 0

print(ans)