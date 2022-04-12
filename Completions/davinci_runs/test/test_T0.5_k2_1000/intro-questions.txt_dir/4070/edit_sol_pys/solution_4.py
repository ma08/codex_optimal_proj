import sys

# check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

# solve the problem
def solve(n):
    # if n is less than 3, there is no prime pair
    if n < 3:
        return 0

    # if n is 3, there is only one prime pair
    elif n == 3:
        return 1
    # if n is greater than 3, we need to find the prime pairs
    else:
        count = 1
        for i in range(3, n, 2):
            if is_prime(i) and is_prime(i+2):
                count += 1
        return count 


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solve(n))
