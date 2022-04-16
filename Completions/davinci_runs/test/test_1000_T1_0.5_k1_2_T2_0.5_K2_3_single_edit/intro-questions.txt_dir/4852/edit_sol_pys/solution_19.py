

import sys

def main():
	# Read the input
	s = sys.stdin.readline()
	s = s.replace("+"," ")
	s = s.split("\n")

	# Convert the input to a list of integers
	s = [int(i) for i in s]

	# Count the number of ways the string can be evaluated
	count = 0
	for i in range(len(s)):
		count += len(s) - i - 1
	print(count)

if __name__ == "__main__":
	main()
