

n = int(input())
q = [int(i) for i in input().split()]

# first and last values of p
p_first = -1
p_last = n - 1

# check if possible
if sum(q) != 0:
	print(-1)
	exit()

# check if possible
for i in q:
	if abs(i) >= n:
		print(-1)
		exit()

# check if possible
for i in range(1, n):
	if q[i] == q[i-1]:
		print(-1)
		exit()

# calculate p
p = [0 for i in range(n)]
for i in range(n-1):
	p[i+1] = p[i] + q[i]

# check if possible
for i in range(n):
	if p[i] > p_last or p[i] < p_first:
		print(-1)
		exit()

# print possible p
print(*p)
