

n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = a[-1]

for i in range(n - 1):
    ans = min(ans, a[i] + a[i + 1])

print(ans)
