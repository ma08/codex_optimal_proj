import sys

num_days = int(sys.stdin.readline().strip())
prices = []
for i in range(num_days):
    price = int(sys.stdin.readline().strip())
    prices.append(price)

prices = sorted(prices)

total_price = 0
for i in range(num_days):
    total_price += prices[i] * (num_days - i)

print(total_price)
