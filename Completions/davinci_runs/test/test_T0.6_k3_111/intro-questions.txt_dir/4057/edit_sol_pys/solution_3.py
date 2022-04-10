
# SOLUTION
n = int(input())
coins = list(map(int, input().split()))

# Start with one pocket and add coin
pockets = [coins.pop(0)]

# Add coin to pockets
for coin in coins:
    # If coin is already in a pocket, add a new pocket
    if coin in pockets:
        pockets.append(coin)
    # If coin is not in a pocket, add it to an existing pocket
    else:
        pocket = pockets[0]
        for i in range(1, len(pockets)):
            if coin not in pockets[i]:
                pocket = pockets[i]
                break
        pockets[pockets.index(pocket)].append(coin)

# Print number of pockets
print(len(pockets))
