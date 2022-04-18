
# Accepted

from math import factorial

def nCr(n,r):
    f = factorial
    return f(n) / f(r) / f(n-r)

def main():
    # Get input
    n = [int(x) for x in input().split()]
    k = int(input())

    # Calculate number of ways to deal cards
    ways = 0
    for i in range(1, k + 1):
        ways += n[i - 1] * nCr(sum(n) - i, k - i)

    # Print number of ways
    print(ways)

if __name__ == '__main__':
    main()
