
n, k = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    ans += i % k == 0
print(ans)
