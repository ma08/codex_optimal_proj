
import sys

def main():
	sys.stdin = open("input.txt", "r")
	sys.stdout = open("output.txt", "w")
	t = int(input())
	for i in range(t):
		n = int(input())
		a = [int(x) for x in input().split()] # list of numbers
		b = [0, 0] # sum of even and odd numbers
		for j in range(n):
			if j % 2 == 0: # if j is even
				b[0] += a[j] # add to even
			else:
				b[1] += a[j] # add to odd
		print(n, b[0], b[1])

if __name__ == "__main__":
	main()
