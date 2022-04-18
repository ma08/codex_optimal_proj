


def next_permutation(s):
	i = len(s) - 1
	while i > 0 and s[i-1] >= s[i]:
		i -= 1
	if i <= 0:
		return False
	j = len(s) - 1
	while s[j] <= s[i-1]:
		j -= 1
	s[i-1], s[j] = s[j], s[i-1]
	s[i:] = s[len(s) - 1 : i-1 : -1]
	return True

def eval(s):
	res = 0
	curr = 0
	for i in range(len(s)):
		if s[i] == 1:
			curr += 1
		else:
			res += curr
			curr = 0
	res += curr
	return res

def num_ways(s):
	count = 0
	for i in range(1, len(s)):
		count += len(s) - i
	return count
import sys

def main():
	# Read the input
	s = sys.stdin.readline()

	# Convert the input to a list of 1s and 0s
	for i in range(len(s)):
		if s[i] == '+':
			s[i] = 1
		else:
			s[i] = 0

	# Count the number of ways the string can be evaluated to a 1
	print(num_ways(s))

	# Find the minimum number of flips
	while next_permutation(s):
		pass
	print(eval(s))

if __name__ == "__main__":
	main()
