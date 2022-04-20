

import sys

def get_primes(n):
    """
    Returns a list of all primes below n.
    """
    primes = [2]
    i = 3
    while i < n:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 2
    return primes


def get_prime_factorization(n, primes):
    """
    Returns a dictionary of the prime factorization of n.
    """
    prime_factorization = {}
    for p in primes:
        if p > n:
            break
        while n % p == 0:
            n //= p
            prime_factorization[p] = prime_factorization.get(p, 0) + 1
    return prime_factorization


def get_prime_factorization_list(numbers, primes):
    """
    Returns a list of the prime factorizations of the numbers.
    """
    prime_factorization_list = []
    for n in numbers:
        prime_factorization_list.append(get_prime_factorization(n, primes))
    return prime_factorization_list


def get_max_primes(prime_factorization_list):
    """
    Returns a dictionary of the maximum exponents of the prime factorizations.
    """
    max_primes = {}
    for p in prime_factorization_list[0]:
        max_primes[p] = prime_factorization_list[0][p]
    for prime_factorization in prime_factorization_list[1:]:
        for p in prime_factorization:
            max_primes[p] = min(max_primes.get(p, 0), prime_factorization[p])
    return max_primes


def get_num_divisors(max_primes):
    """
    Returns the number of divisors of the maximum exponents.
    """
    num_divisors = 1
    for p in max_primes:
        num_divisors *= max_primes[p] + 1
    return num_divisors


def main():
    n = int(sys.stdin.readline())
    numbers = [int(x) for x in sys.stdin.readline().split()]
    primes = get_primes(max(numbers))
    prime_factorization_list = get_prime_factorization_list(numbers, primes)
    max_primes = get_max_primes(prime_factorization_list)
    num_divisors = get_num_divisors(max_primes)
    print(num_divisors)


if __name__ == '__main__':
    main()