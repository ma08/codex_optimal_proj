

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
    if K == N:
        print("You will become a flying monkey!")
        return
    if is_prime(N):
        print("Your wish is granted!")
        return
    if N % 2 == 0:
        if K >= N / 2:
            print("Your wish is granted!")
            return
        print("You will become a flying monkey!")
    print("Your wish is granted!")

if __name__ == '__main__':
    main()
