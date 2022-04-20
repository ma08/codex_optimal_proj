

n, r = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] == 0:
        for j in range(max(0, i - r + 1), min(n, i + r)):
            if a[j] == 1:
                a[i] = 1
                break
    if a[i] == 0:
        ans = -1
        break
    if a[i] == 1:
        ans += 1
print(ans)