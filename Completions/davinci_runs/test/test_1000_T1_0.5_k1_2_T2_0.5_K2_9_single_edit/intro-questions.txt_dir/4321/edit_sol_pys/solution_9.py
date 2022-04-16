

def Minus1(n):
	return n - 1 if n % 10 != 0 else n // 10

def main():
	n,k = map(int, input().split())
	for i in range(k):
		n = Minus1(n)
	print(n)

if __name__ == '__main__':
	main()
