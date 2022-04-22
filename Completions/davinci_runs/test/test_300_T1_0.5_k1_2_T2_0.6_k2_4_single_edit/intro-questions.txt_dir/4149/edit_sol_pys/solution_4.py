

def divisors(n):
    """
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    >>> divisors(28)
    [1, 2, 4, 7, 14]
    """
    i = 1
    result = []
    while i * i < n:
        if n % i == 0:
            result.append(i)
        i += 1
    if i * i == n:
        result.append(i)
    return result + [n // x for x in result[::-1]]


def solve(n, b):
    """
    >>> solve(3, [3, 5, 2, 3, 2, 4])
    [3, 4, 2]
    >>> solve(1, [2750131, 199999])
    [199999]
    >>> solve(1, [3, 6])
    [6]
    """
    # If an element of a is prime, it is replaced by the n-th prime number. It is not replaced by 1.
    # Thus the elements of a cannot be smaller than the n-th prime number.
    # The first n elements of b must be the elements of a.
    # The remaining n elements of b are the divisors of the elements of a. The divisors are smaller than the elements of a.
    # Thus the elements of b can be sorted.
    # All elements of b smaller than the n-th prime number are the divisors of the elements of a.
    # The elements of a are the elements of b that are not smaller than the n-th prime number.
    b.sort(reverse=True)
    a = [i for i in b[:n] if i not in b[n:]]
    return a


if __name__ == "__main__":
    n = int(input())
    b = list(map(int, input().split()))
    print(*solve(n, b))
