
import math

def main():
	n = int(input())
	print(find_cost(n))

def find_cost(n):
	cost = math.inf
	for i in range(1, int(math.sqrt(n)) + 1):
		if n % i == 0:
			if 2 * i + 2 * (n // i) < cost:
				cost = 2 * i + 2 * (n // i)
	return cost

if __name__ == "__main__":
	main()
