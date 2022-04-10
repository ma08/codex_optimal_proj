

def find_common_divisors(numbers):
    """
    Find the number of common divisors of all elements in the array
    :param numbers: an array of numbers
    :return: the number of common divisors
    """
    # Find the GCD of all numbers
    gcd = numbers[0]
    for i in range(1, len(numbers)):
        gcd = gcd_naive(gcd, numbers[i])

    # Find the number of divisors of the GCD
    return find_divisors(gcd)


def gcd_naive(a, b):
    """
    Find the greatest common divisor of two numbers
    :param a: first number
    :param b: second number
    :return: the greatest common divisor
    """
    if b == 0:
        return a
    else:
        return gcd_naive(b, a % b)


def find_divisors(n):
    """
    Find the number of divisors of a number
    :param n: a number
    :return: the number of divisors
    """
    divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors += 1

    return divisors


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(find_common_divisors(numbers))