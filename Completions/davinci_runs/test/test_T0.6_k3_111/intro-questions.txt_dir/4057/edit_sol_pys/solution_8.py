n = int(input())

coins = list(map(int, input().split()))
coins.sort()

count = 1
last = coins[0]
for coin in coins:
    if coin != last:
        count += 1
    last = coin

print(count)
