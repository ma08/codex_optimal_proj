

import sys

def main():
	n, k = map(int, sys.stdin.readline().strip().split())
	a = map(int, sys.stdin.readline().strip().split())
	
	if n < k:
		print 'NO'
		return
	
	c = [0] * n
	
	d = {}
	
	for i in xrange(n):
		if a[i] not in d:
			d[a[i]] = []
		d[a[i]].append(i)
	
	curr_color = 1
	
	for i in xrange(1, n+1):
		if i not in d:
			continue
		
		for j in d[i]:
			c[j] = curr_color
		
		curr_color += 1
		if curr_color > k:
			curr_color = 1
	
	print 'YES'
	print ' '.join(map(str, c))

if __name__ == '__main__':
	main()