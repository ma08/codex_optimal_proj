


def get_nth_prime(n):
    """
    >>> get_nth_prime(1)
    2
    >>> get_nth_prime(2)
    3
    >>> get_nth_prime(3)
    5
    """
    primes = [2]
    i = 3
    while len(primes) < n:
        if all(i % p != 0 for p in primes):
            primes.append(i)
        i += 1
    return primes[-1]


def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    """
    if n == 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def solve(n, b):
    """
    >>> solve(3, [3, 5, 2, 3, 2, 4])
    [3, 4, 2]
    >>> solve(1, [2750131, 199999])
    [199999]
    >>> solve(1, [3, 6])
    [6]
    """
    # The first n elements of b are the elements of a.
    # The remaining n elements of b are the divisors of the elements of a.
    # If an element of a is prime, it is replaced by the n-th prime number.
    # Thus the elements of b can be sorted and the second half of the elements of b can be used to find the elements of a.
    # The elements of a are the elements of b that are not in the second half of b.
    b.sort()
    a = [i if is_prime(i) else get_nth_prime(i) for i in b if i not in b[n:]]
    return a


if __name__ == "__main__":
    n = int(input())
    b = list(map(int, input().split()))
    print(*solve(n, b))
