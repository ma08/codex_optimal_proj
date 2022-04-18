
n = int(input())

def sum_digits(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s

while n % sum_digits(n) != 0:
    n += 1
print(n)
