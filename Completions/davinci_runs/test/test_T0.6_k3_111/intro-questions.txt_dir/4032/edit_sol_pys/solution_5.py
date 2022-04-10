n, k = map(int, input().split())
a = list(map(int, input().split()))[::-1]
ans = 0

while True:
    if a[-1] <= k:
        ans += 1
        a.pop()
    elif a[0] <= k:
        ans += 1
        a.pop(0)
    else:
        break

print(ans)
