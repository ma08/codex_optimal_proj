

from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# def get_primes(n):
#     prime_list = []
#     for i in range(2, n):
#         if is_prime(i):
#             prime_list.append(i)
#     return prime_list

def get_primes(n):
    prime_list = [2, 3]
    i = 1
    while len(prime_list) < n:
        i += 6
        if is_prime(i):
            prime_list.append(i)
        i += 4
        if is_prime(i):
            prime_list.append(i)
    return prime_list

def get_divisor(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i
    return 1

def get_a(b):
    a = []
    for i in range(len(b) // 2):
        if is_prime(b[i]):
            a.append(b[i])
        else:
            a.append(b[i] // get_divisor(b[i]))
    return a

def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    a = get_a(b)
    print(' '.join([str(x) for x in a]))

if __name__ == '__main__':
    main()