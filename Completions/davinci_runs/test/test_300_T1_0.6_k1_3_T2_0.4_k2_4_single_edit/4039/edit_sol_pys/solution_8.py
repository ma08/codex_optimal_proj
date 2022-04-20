

def main():
	n, r = map(int, input().split())
	a = []
	b = []
	for i in range(n):
		c, d = map(int, input().split())
		a.append(c)
		b.append(d)

	for i in range(n):
		if r < a[i]: print('NO'); break
		r += b[i]
		if r < 0: print('NO'); break
		if i == n - 1: print('YES')

if __name__ == '__main__':
	main()
