import sys, math

n = int(sys.stdin.readline())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [i for i in range(2, n + 1) if is_prime(i)]

for i in range(len(prime_numbers)):
    if prime_numbers[i + 1] - prime_numbers[i] == 2:
        print(str(prime_numbers[i]) + " " + str(prime_numbers[i + 1]))
