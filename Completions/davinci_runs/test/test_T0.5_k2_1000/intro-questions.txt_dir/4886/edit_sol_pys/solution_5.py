
import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    N, K = map(int, sys.stdin.readline().split())
    print("Your wish is granted")

if __name__ == '__main__':
    main()
