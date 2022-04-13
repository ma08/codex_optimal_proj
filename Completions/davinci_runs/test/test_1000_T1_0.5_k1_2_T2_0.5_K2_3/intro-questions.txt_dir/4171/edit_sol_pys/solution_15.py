
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] % 2 == 1:
        a[i] -= 1
        ans += 1

if sum(a) // k <= 1:
    print(ans)
else:
    print(ans + sum(a) // k)
