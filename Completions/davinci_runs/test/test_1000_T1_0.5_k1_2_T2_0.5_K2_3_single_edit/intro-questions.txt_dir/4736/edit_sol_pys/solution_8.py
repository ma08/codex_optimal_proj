
# Accepted

from math import factorial

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def main():
    # Get input
    n = [int(x) for x in input().split()]
    k = int(input())

    # Calculate number of ways to deal cards
    ways = sum(n[i - 1] * nCr(sum(n) - i, k - i) for i in range(1, k + 1))

    # Print number of ways
    print(ways)

if __name__ == '__main__':
    main()
