
import sys

def combinations(n, r):
    """
    Calculate combinations with repetitions
    """
    if n < 0 or r < 0 or n < r:
        return 0
    return factorial(n + r - 1) // factorial(r) // factorial(n - 1)

def factorial(n):
    """
    Calculate factorial
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    """
    main function
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    mod = 10 ** 9 + 7
    print(combinations(n + m - 1, n - 1) % mod)

if __name__ == "__main__":
    main()
