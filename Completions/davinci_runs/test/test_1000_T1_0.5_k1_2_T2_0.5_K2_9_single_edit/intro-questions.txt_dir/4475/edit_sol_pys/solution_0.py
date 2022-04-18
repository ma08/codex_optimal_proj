


def main():
	t = int(input())
	for i in range(t):
		a, b, x, y, n = map(int, input().split())
		if a == x:
			b = max(y, b - n)
		elif b == y:
		elif a - x > b - y:
			a = max(x, a - n)
			b = max(y, b - n)
		elif a - x < b - y:
			b = max(y, b - n)
			a = max(x, a - n)
			a = max(x, a - n)
		else:
			a = max(x, a - n)
			b = max(y, b - n)
		print(a * b)


if __name__ == '__main__':
	main()
