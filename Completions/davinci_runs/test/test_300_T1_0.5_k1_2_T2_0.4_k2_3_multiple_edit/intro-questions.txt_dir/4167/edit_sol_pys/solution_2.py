
n, k = map(int,input().split())
ans = 0
for i in range(1, k+1):
    if i <= n:
        ans += n - i + 1
print(ans**3)
