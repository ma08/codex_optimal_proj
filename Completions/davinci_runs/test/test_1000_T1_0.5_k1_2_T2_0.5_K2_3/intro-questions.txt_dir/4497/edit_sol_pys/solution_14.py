

n, m = map(int, input().split())

a = list(map(int, input().split()))

ans = [0] * n

for i in range(m):
    l, r, k = map(int, input().split())
    ans[l-1] += k
    ans[r] -= k


tmp = 0
for i in range(n):
    tmp += ans[i]
    ans[i] = tmp

print(max(ans))
