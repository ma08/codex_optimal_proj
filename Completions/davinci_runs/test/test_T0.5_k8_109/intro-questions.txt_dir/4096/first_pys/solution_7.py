

# Solution

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 1

for i in range(n):
	ans = max(ans, (a[i] + i) // (i + 1))

if (ans * (n + 1) < m):
	print(-1)
else:
	print(ans)