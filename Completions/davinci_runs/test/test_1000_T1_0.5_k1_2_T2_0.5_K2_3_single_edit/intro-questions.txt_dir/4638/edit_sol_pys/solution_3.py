
n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = [0] * n
for i in range(1, n):
    ans[i] = min(ans[i - 1] + a[i - 1], ans[i - 2] + c + b[i - 2])

print(*ans)
