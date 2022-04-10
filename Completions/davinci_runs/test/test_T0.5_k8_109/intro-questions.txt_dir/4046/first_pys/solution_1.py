

def main(n, q):
	if n == 2:
		if abs(q[0]) == 1:
			print (1, q[0]+1)
		else:
			print (-1)
	else:
		p = [0] * n
		p[0] = q[0]
		for i in range(1, n-1):
			p[i] = q[i] + p[i-1]
		p[n-1] = -p[n-2]
		for i in range(n):
			if p[i] < 1 or p[i] > n:
				print (-1)
				return
		print (*p)

if __name__ == '__main__':
	n = int(input())
	q = list(map(int, input().split()))
	main(n, q)