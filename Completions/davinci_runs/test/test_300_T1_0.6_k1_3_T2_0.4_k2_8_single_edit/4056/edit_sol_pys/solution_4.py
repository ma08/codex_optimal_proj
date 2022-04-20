
from collections import Counter

def gcd(a, b):
	if (b == 0):
		return a
	return gcd(b, a % b)

def get_prime_factors(n):
	factors = Counter()

	while (n % 2 == 0):
		factors[2] += 1
		n /= 2

	for i in range(3, int(n**0.5) + 1, 2):
		while (n % i == 0):
			factors[i] += 1
			n /= i

	if (n > 2):
		factors[n] += 1

	return factors


if __name__ == '__main__':
	_ = input()
	arr = list(map(int, input().split()))

	n = len(arr)

	gcd_so_far = arr[0]
	for i in range(1, n):
		gcd_so_far = gcd(gcd_so_far, arr[i])

	if (gcd_so_far == 1):
		print(1)
	else:
		factors = get_prime_factors(gcd_so_far)
		print(len(factors))
