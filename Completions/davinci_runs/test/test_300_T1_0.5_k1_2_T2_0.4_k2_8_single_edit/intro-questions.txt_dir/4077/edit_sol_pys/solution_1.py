
import sys

def median(nums):
	n = len(nums)
	if n < 1:
		return None
	if n % 2 == 1:
		return sorted(nums)[n//2]
	else:
		return sum(sorted(nums)[n//2-1:n//2+1])/2.0

def main():
	n, m = [int(x) for x in sys.stdin.readline().split()]
	nums = [int(x) for x in sys.stdin.readline().split()]
	pairs = 0
	for i in range(n):
		for j in range(i, n):
			if median(nums[i:j+1]) == m:
				pairs += 1
	print(pairs)

if __name__ == '__main__':
	main()
