
#!/usr/bin/env python

from math import factorial

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def main():
    # Get input, k cards to deal
    n = [int(x) for x in raw_input().split()]
    k = int(raw_input())

    # Calculate number of ways to deal cards
    ways = 0
    for i in range(1, k + 1):
        ways += n[i - 1] * nCr(sum(n) - i, k - i)

    # Print number of ways
    print(ways)

if __name__ == '__main__':
    main()
