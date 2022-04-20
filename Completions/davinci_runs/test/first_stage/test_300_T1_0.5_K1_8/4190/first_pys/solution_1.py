

def function(n, a, b):
	c = []
	for i in range(n):
		c.append((a[i] + b[i]) % n)
	c.sort()
	return c

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = function(n, a, b)
print(*c)