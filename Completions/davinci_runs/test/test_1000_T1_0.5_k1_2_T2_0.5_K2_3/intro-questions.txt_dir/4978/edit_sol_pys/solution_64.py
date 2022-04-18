#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:57:03 2020

@author: konrad
"""

"""

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

for row in range(N):
    for col in range(M):
        if grid[row][col] == "V":
            if row == 0:
                pass
            elif grid[row-1][col] == ".":
                grid[row-1][col] = "V"
            elif grid[row-1][col] == "#":
                if col > 0 and grid[row][col-1] == ".":
                    grid[row][col-1] = "V"
                if col < M-1 and grid[row][col+1] == ".":
                    grid[row][col+1] = "V"

for row in range(N):
    print("".join(grid[row]))
"""


def find_prime_factors(number):
    """
    Finds all the prime factors of a positive integer
    Args:
        number(int): Number to find prime factors
    Returns:
        list: List containing prime factors
    """
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number /= divisor
        else:
            divisor += 1
    return factors


def find_unique_prime_factors_with_count(number):
    """
    Finds all the unique prime factors of a positive integer and the
    count of those prime factors
    Args:
        number(int): Number to find prime factors
    Returns:
        list: List containing prime factors and their count
    """
    factors = {}
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            if divisor not in factors:
                factors[divisor] = 0
            factors[divisor] += 1
            number /= divisor
        else:
            divisor += 1
    return factors


def find_largest_prime_factor(number):
    """
    Finds the largest prime factor of a positive integer
    Args:
        number(int): Number to find largest prime factor
    Returns:
        int: Largest prime factor
    """
    largest_factor = 1
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            largest_factor = divisor
            number /= divisor
        else:
            divisor += 1
    return largest_factor


def is_prime(number):
    """
    Checks if the number is prime
    Args:
        number(int): Number to check
    Returns:
        bool: True if number is prime, else False
    """
    if number == 1:
        return False
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def find_prime_number(number):
    """
    Finds the nth prime number
    Args:
        number(int): The nth number to find
    Returns:
        int: The nth prime number
    """
    prime_numbers_list = []
    prime_count = 0
    candidate = 2
    while prime_count < number:
        if is_prime(candidate):
            prime_count += 1
            prime_numbers_list.append(candidate)
        candidate += 1
    return prime_numbers_list[-1]


def find_prime_in_range(start, end):
    """
    Finds all the prime numbers in a given range
    Args:
        start(int): Starting number
        end(int): Ending number
    Returns:
        list: List of prime numbers
    """
    prime_numbers_list = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers_list.append(num)
    return prime_numbers_list


def find_nth_fibonacci_number(number):
    """
    Finds the nth fibonacci number
    Args:
        number(int): nth number to find
    Returns:
        int: The nth fibonacci number
    """
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < number + 1:
        fibonacci_numbers.append(0)
    if number == 1:
        return fibonacci_numbers[1]
    else:
        if fibonacci_numbers[number - 1] == 0:
            fibonacci_numbers[number - 1] = find_nth_fibonacci_number(
                number - 1)
        if fibonacci_numbers[number - 2] == 0:
            fibonacci_numbers[number - 2] = find_nth_fibonacci_number(
                number - 2)
        fibonacci_numbers[number] = fibonacci_numbers[number - 2] + \
            fibonacci_numbers[number - 1]
    return fibonacci_numbers[number]


def find_fibonacci_in_range(start, end):
    """
    Finds all fibonacci numbers in a given range
    Args:
        start(int): Starting number
        end(int): Ending number
    Returns:
        list: List of fibonacci numbers
    """
    fibonacci_numbers = []
    for num in range(start, end + 1):
        fibonacci_numbers.append(find_nth_fibonacci_number(num))
    return fibonacci_numbers


def find_factorial(number):
    """
    Finds the factorial of a number
    Args:
        number(int): Number to find factorial
    Returns:
        int: Factorial of a number
    """
    factorial = 1
    if number < 0:
        return "Factorial doesn't exist for negative numbers"
    elif number == 0:
        return 1
    else:
        for num in range(1, number + 1):
            factorial = factorial * num
        return factorial
