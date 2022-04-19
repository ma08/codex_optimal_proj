
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] % 2 == 1:
        a[i] -= 1
        ans += 1

print(ans + (sum(a) - 1) // k)
