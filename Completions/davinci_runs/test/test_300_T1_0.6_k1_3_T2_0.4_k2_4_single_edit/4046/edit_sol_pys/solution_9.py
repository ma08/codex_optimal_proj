

n = int(input())
q = [int(i) for i in input().split()]

# first and last values of p (inclusive)
p_first = 0
p_last = n - 1

# check if possible (sum of q must be 0)
if sum(q) != 0: print(-1); exit()

# check if possible (all values of q must be in range)
for i in q:
	if abs(i) >= n: print(-1); exit()

# check if possible (no two consecutive values of q are equal)
for i in range(1, n):
	if q[i] == q[i-1]: print(-1); exit()

# calculate p
p = [0 for i in range(n)]
for i in range(n-1):
	p[i+1] = p[i] + q[i]

# check if possible (all values of p must be in range)
for i in p:
	if i > p_last or i < p_first: print(-1); exit()

# print possible p
print(*p)
