
import sys

def combination(n, r):
    """
    Calculate combination with repetition
    """
    if n < 0 or r < 0 or n < r:
        return 0
    return factorial(n + r - 1) // factorial(r) // factorial(n - 1) % mod

def factorial(n):
    """
    Calculate factorials
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
    print(combination(n + m - 1, n - 1))

if __name__ == "__main__":
    main()
