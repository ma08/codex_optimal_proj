

n,m = map(int,input().split())
s = [0]*n
d = [0]*n
c = [0]*n
for i in range(m):
	s[i],d[i],c[i] = map(int,input().split())
	s[i] -= 1
	d[i] -= 1
	c[i] -= 1

for i in range(m):
	if c[i] > d[i] - s[i]:
		print(-1)
		exit()

a = [0]*n
for i in range(m):
	if c[i] == 0:
		a[d[i]] = i+1
		continue
	for j in range(s[i],d[i]):
		if a[j] != 0:
			print(-1)
			exit()
	a[s[i]] = i+1
	a[d[i]] = i+1
	c[i] -= 1
	for j in range(s[i]+1,d[i]):
		if c[i] == 0:
			break
		if a[j] != 0:
			print(-1)
			exit()
		a[j] = i+1
		c[i] -= 1
	if c[i] != 0:
		print(-1)
		exit()

for i in range(n):
	if a[i] == 0:
		a[i] = m+1

print(*a)