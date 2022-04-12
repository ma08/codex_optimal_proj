

# Accepted

from math import factorial

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def main():
    # Get input
    n = [int(x) for x in input().split()] # n = [1, 2, 3, 4]
    k = int(input()) # k = 3

    # Calculate number of ways to deal cards
    ways = 0 # ways = 0
    for i in range(1, k + 1):
        ways += n[i - 1] * nCr(sum(n) - i, k - i) # ways = 1 * nCr(10, 2)

    # Print number of ways
    print(ways)

if __name__ == '__main__':
    main()
