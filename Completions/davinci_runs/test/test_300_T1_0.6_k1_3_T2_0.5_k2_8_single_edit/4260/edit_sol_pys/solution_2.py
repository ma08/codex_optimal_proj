

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n - 2):
    if a[i] < a[i + 1] < a[i + 2] or a[i] > a[i + 1] > a[i + 2]:
        ans += 1

print(ans)
