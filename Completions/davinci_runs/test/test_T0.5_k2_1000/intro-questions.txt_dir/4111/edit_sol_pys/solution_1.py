
n, k = map(int, input().split())
a = list(map(int, input().split())) 
a.sort()

ans = 0
for i in range(n):
    if a[i] == 0:
        ans += 1
    elif a[i] <= k:
        k -= a[i]
        ans += 1

print(ans)
