

def isPrime(n):
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True

def getPrime(n):
	if n == 1:
		return 2
	i = 1
	v = 3
	while i < n:
		if isPrime(v):
			i += 1
		v += 2
	return v - 2

def solve(n, b):
	a = []
	i = 0
	while i < len(b):
		if b[i] == b[i + 1]:
			a.append(b[i])
			i += 1
		else:
			p = getPrime(b[i + 1])
			a.append(p)
		i += 1
	return a

def main():
	n = int(input())
	b = list(map(int, input().split()))
	a = solve(n, b)
	print(' '.join(map(str, a)))

if __name__ == '__main__':
	main()