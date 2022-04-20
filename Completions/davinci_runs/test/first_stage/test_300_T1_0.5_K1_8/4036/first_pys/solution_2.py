

def solve(n,k):
	if n <= 1:
		print "YES"
		print n
		return
	if k == 1 and n!=1:
		print "NO"
		return
	if n == 2:
		print "YES"
		print 1,1
		return
	if k == 2 and n>=3:
		print "YES"
		print 2,n-2
		return
	print "YES"
	a = [1]
	for i in range(1,k):
		a.append(2*a[i-1])
		n -= a[i]
		if n <= a[i]:
			a[i] += n
			break
	print " ".join(map(str,a))

n,k = map(int,raw_input().split())
solve(n,k)