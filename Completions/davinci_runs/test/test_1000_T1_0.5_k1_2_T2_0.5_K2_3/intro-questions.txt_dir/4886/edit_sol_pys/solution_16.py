

import sys, math

    """
    Check if n is a prime
    """
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

    """
    Print the result
    """
def main():
    N, K = map(int, sys.stdin.readline().split())
    if K == 0:
        print("Your wish is granted!")
    elif K == N:
        print("You will become a flying monkey!") 
    elif N <= 3:
        print("Your wish is granted!")
    else:
        if is_prime(N):
            print("Your wish is granted!")
        elif N % 2 == 0:
            if K >= N // 2:
                print("Your wish is granted!")
            else:
                print("You will become a flying monkey!")
        else:
            print("Your wish is granted!")

if __name__ == '__main__':
    main()
