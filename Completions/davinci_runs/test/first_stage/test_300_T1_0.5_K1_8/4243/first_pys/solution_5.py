

x = int(input())

coins = [500, 100, 50, 10, 5, 1]

total = 0
for coin in coins:
    total += x // coin
    x %= coin

print(total)