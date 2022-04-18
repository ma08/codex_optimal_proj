
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    print(solve(n, k))

def solve(n, k):
    """
    Return the number of times a person must take a drink.
    """
    count = 0
    while n > 0:
        count += n % k
        n //= k
    return count

if __name__ == '__main__':
    main()
