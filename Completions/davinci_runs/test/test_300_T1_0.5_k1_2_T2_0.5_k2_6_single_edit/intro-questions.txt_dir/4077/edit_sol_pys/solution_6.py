import sys

def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0

def main():
	n, m = [int(x) for x in sys.stdin.readline().split()]
	lst = [int(x) for x in sys.stdin.readline().split()]
	pairs = 0
	for i in range(n):
		for j in range(i, n):
			if median(lst[i:j+1]) == m:
				pairs += 1
	print(pairs)

if __name__ == '__main__':
	main()
