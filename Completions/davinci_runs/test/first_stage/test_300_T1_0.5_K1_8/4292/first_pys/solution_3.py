

import sys

def main():
    # Read the number of items and the number of items to choose
    N, K = sys.stdin.readline().split()
    N = int(N)
    K = int(K)

    # Read the price of each item
    prices = sys.stdin.readline().split()
    prices = [int(p) for p in prices]

    # Sort the prices in ascending order
    prices.sort()

    # The minimum total price is the sum of the K cheapest items
    print(sum(prices[:K]))

if __name__ == '__main__':
    main()