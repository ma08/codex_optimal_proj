

n,k = map(int,input().split())

if k*2 < n or (n%k != 0 and n%k != 1):
	print("NO")
else:
	a = []
	c = 0
	for i in range(1,k+1):
		a.append(i)
		c += i
		if c >= n:
			a[-1] += n-c
			break
		if c == n-1:
			a[-1] += 1
			break
	print("YES")
	print(*a)