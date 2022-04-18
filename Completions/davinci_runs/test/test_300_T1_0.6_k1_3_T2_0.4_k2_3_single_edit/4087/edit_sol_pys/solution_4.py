

def get_digit_sum(n):
	"""
	Return the sum of the digits of n
	"""
	digit_sum = 0
	while n > 0:
		digit_sum += n % 10
		n //= 10
	return digit_sum

def is_interesting(n):
	"""
	Return True if the sum of the digits of n is divisible by 4
	"""
	return get_digit_sum(n) % 4 == 0

def get_nearest_interesting(n):
	"""
	Return the nearest interesting number greater or equal to n
	"""
	if is_interesting(n):
		return n
	elif is_interesting(n + 1):
		return n + 1
	else:
		return get_nearest_interesting(n + 1)

n = int(raw_input())
print get_nearest_interesting(n)
