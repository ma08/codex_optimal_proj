
def solve(n, b):
    """
    >>> solve(3, [3, 5, 2, 3, 2, 4, 2, 4, 5, 7, 2, 11, 5, 7, 11, 13, 5, 17, 7, 11, 13, 17, 19, 7, 23])
    [3, 4, 2]
    >>> solve(1, [2750131, 199999, 199999, 2750131])
    [199999, 2750131]
    >>> solve(1, [3, 6, 6, 3])
    [6, 3]
    """
    # The first n elements of b are the elements of a.
    # The remaining n elements of b are the prime divisors of the elements of a.
    # If an element of a is prime, it is replaced by the n-th prime number in the sorted list of elements of b.
    # Thus the elements of b can be sorted and the second half of the elements of b can be used to find the elements of
    # a.
    # The elements of a are the elements of b that are not in the second half of b and are not divisible by any primes
    # in the second half of b.
    b.sort()
    a = [i for i in b if i not in b[n:] and all([i % j != 0 for j in b[n:]])]
    return a


if __name__ == "__main__":
    n = int(input())
    b = list(map(int, input().split()))
    print(*solve(n, b))
