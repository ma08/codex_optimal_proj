

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

while True:
    if a[0] <= k:
        ans += 1
        a.pop(0)
    elif a[-1] <= k:
        ans += 1
        a.pop()
    else:
        break

print(ans)