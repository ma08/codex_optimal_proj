

def main():
	n = int(input())

	print(len(set(next(n) for _ in range(20))))

def next(n):
	n += 1

	while n % 10 == 0:
		n //= 10

	return n

if __name__ == '__main__':
	main()