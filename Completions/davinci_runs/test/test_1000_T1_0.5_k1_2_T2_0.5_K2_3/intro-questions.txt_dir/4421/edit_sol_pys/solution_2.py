
n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()


def possible(a, b) -> bool:
	return (a + b) % k == 0

ans = 0
l, r = 0, n - 1
while l < r:
	if possible(a[l], a[r]):
		ans += 2
		l += 1
		r -= 1
	else:
		ans += 1
		r -= 1

if l == r:
	ans += 1

print(ans)
