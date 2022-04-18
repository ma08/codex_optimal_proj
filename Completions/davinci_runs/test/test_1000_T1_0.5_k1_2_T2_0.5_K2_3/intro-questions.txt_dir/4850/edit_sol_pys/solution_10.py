

# Accepted after 1 submission

def max_coins(coins):
    """Returns the maximum number of coins you can take."""
    # TODO
    return 0

def main():
    # Read input, split into list of coins
    coins = input().split()
    coins = [int(coin) for coin in coins]
    
    # Calculate and print output
    print(max_coins(coins))

if __name__ == "__main__":
    main()
