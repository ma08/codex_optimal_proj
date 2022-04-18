

n = int(input()) # number of elements
q = [int(i) for i in input().split()] # q values

# first and last values of p (possible)
p_first = 1
p_last = n+1

# check if possible (sum of q)
if sum(q) != 0:
	print(-1)
	exit()

# check if possible (abs(q[i]) < n)
for i in q:
	if abs(i) >= n:
		print(-1)
		exit()

# check if possible (q[i] != q[i-1])
for i in range(1, n):
	if q[i] == q[i-1]:
		print(-1)
		exit()

# calculate p
p = [0 for i in range(n)]
for i in range(n-1):
	p[i+1] = p[i] + q[i]

# check if possible (p[i] < p_last and p[i] > p_first)
for i in p:
	if i > p_last or i < p_first:
		print(-1)
		exit()

# print possible p
print(*p)
