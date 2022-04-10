n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

while True:
    if len(a) == 0:
        break
    elif a[0] <= k:
        ans += 1
        a.pop(0)
    elif a[-1] <= k: 
        ans += 1
        a.pop()

print(ans)
