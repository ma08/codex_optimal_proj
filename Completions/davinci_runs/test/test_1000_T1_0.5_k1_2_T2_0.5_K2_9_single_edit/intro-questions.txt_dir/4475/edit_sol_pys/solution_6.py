


def main():
	t = int(input())
	for i in range(t):
		a, b, x, y, n = map(int, input().split())
		if a == x:
			b = max(y, b - n)
		elif b == y:
			a = max(x, a - n)
		else:
			n1 = n
			a1 = a
			b1 = b
			while n > 0 and a > x and b > y:
				if a - x > b - y:
					a -= 1
					n -= 1
				else:
					b -= 1
					n -= 1
			if n > 0:
				if a > x:
					a -= n
				else:
					b -= n
			a = max(x, a)
			b = max(y, b)
			n1 -= n
			a1 = max(x, a1 - n1)
			b1 = max(y, b1 - n1)
		print(min(a * b, a1 * b1))


if __name__ == '__main__':
	main()
