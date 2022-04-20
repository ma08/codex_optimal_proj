import sys, math

def find_bad_prices(prices):
	stack = []
	bad_prices = 0
	for i in range(len(prices)):
		while stack and prices[i] < prices[stack[-1]]:
			bad_price = stack.pop()
			bad_prices += 1
		stack.append(i)
	return bad_prices

if __name__ == "__main__":
	t = int(input().strip())
	for a0 in range(t):
		n = int(input().strip())
		prices = list(map(int, input().strip().split(' ')))
		print(find_bad_prices(prices))