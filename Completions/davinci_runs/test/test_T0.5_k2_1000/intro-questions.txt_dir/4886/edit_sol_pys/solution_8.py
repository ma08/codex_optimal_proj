
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
    if K == 0 or N <= 4:
        print("Your wish is granted")
    elif K == N:
        print("You will become a flying monkey!")
    else:
        if is_prime(N):
            print("Your wish is granted")
        elif N % 2 == 0:
            if K >= N / 2:
                print("Your wish is granted")
            else:
                print("You will become a flying monkey!")
        else:
            print("Your wish is granted")

if __name__ == '__main__':
    main()
