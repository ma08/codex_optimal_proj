import sys

def combinations(n, m):
    """
    Calculate combinations with repetition
    """
    if n < 0 or m < 0 or n < m:
        return 0
    return factorial(n + m - 1) // factorial(m) // factorial(n - 1)

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
