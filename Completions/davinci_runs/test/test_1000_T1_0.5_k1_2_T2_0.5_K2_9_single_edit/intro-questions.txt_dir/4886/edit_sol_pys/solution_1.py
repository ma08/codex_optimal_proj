

import sys, math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_power_of_2(n):
    return n > 0 and ((n & (n - 1)) == 0)


def main():
    N, K = map(int, sys.stdin.readline().split())
    if K == 0 or is_power_of_2(N):
        print("Your wish is granted!")
    elif K == N:
        print("You will become a flying monkey!")
    else:
        print("You will become a flying monkey!")

if __name__ == '__main__':
    main()
