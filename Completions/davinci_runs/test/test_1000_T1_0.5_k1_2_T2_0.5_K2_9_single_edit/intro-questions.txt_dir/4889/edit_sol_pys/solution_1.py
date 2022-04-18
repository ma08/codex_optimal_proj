import math

import sys

def main():
    # Read the number of coins
    N = int(sys.stdin.readline()) 

    # Read the values of the coins
    coins = []
    for i in range(N):
        coins.append(int(sys.stdin.readline()))

    # Sort the coins from lowest to highest value
    coins.sort()

    # Iterate over the coins
    while len(coins) > 1:
        # Fuse the two lowest valued coins
        coins[0] = coins[0] + coins[1] - 1
        # Remove the second lowest valued coin
        del coins[1]
        # Sort the coins from lowest to highest value
        coins.sort()

    # Print the value of the resulting coin
    print(coins[0])

if __name__ == "__main__":
    main()
