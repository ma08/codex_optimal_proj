
def solve(s, k):
	n = len(s)
	i = 0
	while i < n and s[i] == s[0]:
		i += 1
	if i == n:
		return s * (k // n) + s[:k % n]
	else:
		return s * k

n, k = map(int, input().split())
s = input()
print(solve(s, k))
