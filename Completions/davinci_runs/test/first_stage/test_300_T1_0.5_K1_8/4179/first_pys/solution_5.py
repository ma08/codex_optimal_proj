

n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    if sum(map(lambda x, y: x * y, a[i], b)) + c > 0:
        ans += 1
print(ans)