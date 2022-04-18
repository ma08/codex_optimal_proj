
n = int(input())

a = [int(x) for x in input().split()]

a.sort()

l = 0
r = 0
m = 0
for i in range(n):
	while l <= r and a[i] - a[l] > 5:
		l += 1
	r += 1
	m = max(m, r - l)
print(m)
