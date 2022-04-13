
import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_emirp(n):
    if is_prime(n) and is_palindrome(n):
        return False
    return is_prime(int(str(n)[::-1]))


def prime_count(n):
    count = 0
    for i in range(1, n+1):
        if is_prime(i):
            count += 1
    return count


def is_perfect(n):
    if n <= 1:
        return False
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i * i != n:
                sum = sum + i + n / i
            else:
                sum = sum + i
        i += 1
    return sum == n


def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)


def is_perfect_square(n):
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n


def is_happy(n):
    while n != 1 and n != 4:
        n = sum(int(i)**2 for i in str(n))
    return n == 1
