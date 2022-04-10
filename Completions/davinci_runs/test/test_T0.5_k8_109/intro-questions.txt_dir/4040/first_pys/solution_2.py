

n,m,d=map(int,input().split())
c=list(map(int,input().split()))

# n,m,d=10,1,11
# c=[1]

# n,m,d=7,3,2
# c=[1,2,1]

# n,m,d=10,1,5
# c=[2]

def ispossible(n,m,d,c):
	if m==1:
		if c[0]<=d:
			return True
		else:
			return False
	else:
		if m==2:
			if c[0]+c[1]<=d:
				return True
			else:
				return False
		else:
			if c[0]+c[1]<=d:
				return True
			else:
				return False

if ispossible(n,m,d,c):
	print('YES')
	a=[0]*(n)
	for i in range(m):
		for j in range(c[i]):
			a[j]=i+1
	print(*a)
else:
	print('NO')