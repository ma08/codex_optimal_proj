

# Solution

q = int(input())
for i in range(q):
	k = int(input())
	n = int(k**0.5)
	if n*(n+1) < k:
		n+=1
	k -= n*(n-1)
	print(str(n)[k-1])