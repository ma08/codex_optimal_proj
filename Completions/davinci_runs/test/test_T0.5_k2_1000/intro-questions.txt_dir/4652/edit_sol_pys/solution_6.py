#!/bin/python3
import sys
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def get_prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            if is_prime(i):
                factors.append(i)
    return factors
def get_prime_factors_count(n):
    factors = get_prime_factors(n)
    factors_count = []
    for i in factors:
        count = 0
        while n % i == 0:
            count += 1
            n /= i
        factors_count.append(count)
    return factors_count
def get_factorial_factors_count(n):
    factors_count = []
    for i in range(2, n + 1):
        factors = get_prime_factors_count(i)
        for j in range(len(factors)):
            if j < len(factors_count):
                factors_count[j] += factors[j]
            else:
                factors_count.append(factors[j])
    return factors_count
def get_factorial_factors_count_upto(n):
    factors_count = []
    for i in range(2, n + 1):
        factors = get_prime_factors_count(i)
        for j in range(len(factors)):
            if j < len(factors_count):
                factors_count[j] += factors[j]
            else:
                factors_count.append(factors[j])
    return factors_count
def get_factorial_factors_count_upto_modulo(n, modulo):
    factors_count = []
    for i in range(2, n + 1):
        factors = get_prime_factors_count(i)
        for j in range(len(factors)):
            if j < len(factors_count):
                factors_count[j] = (factors_count[j] + factors[j]) % modulo
            else:
                factors_count.append(factors[j] % modulo)
    return factors_count
def get_factorial_factors_count_upto_modulo_factorial(n, modulo):
    factors_count = []
    for i in range(2, n + 1):
        factors = get_prime_factors_count(i)
        for j in range(len(factors)):
            if j < len(factors_count):
                factors_count[j] = (factors_count[j] * pow(factors[j], modulo - 2, modulo)) % modulo
            else:
                factors_count.append(pow(factors[j], modulo - 2, modulo))
    return factors_count
def get_factorial_factors_count_upto_modulo_factorial_factorial(n, modulo):
    factors_count = []
    for i in range(2, n + 1):
        factors = get_prime_factors_count(i)
        for j in range(len(factors)):
            if j < len(factors_count):
                factors_count[j] = (factors_count[j] * pow(factors[j], modulo - 2, modulo)) % modulo
            else:
                factors_count.append(pow(factors[j], modulo - 2, modulo))
    return factors_count
def get_factorial_factors_count_upto_modulo_factorial_factorial_factorial(n, modulo):
    factors_count = []
    for i in range(2, n + 1):
        factors = get_prime_factors_count(i)
        for j in range(len(factors)):
            if j < len(factors_count):
                factors_count[j] = (factors_count[j] * pow(factors[j], modulo - 2, modulo)) % modulo
            else:
                factors_count.append(pow(factors[j], modulo - 2, modulo))
    return factors_count
def get_factorial_factors_count_upto_modulo_factorial_factorial_factorial_factorial(n, modulo):
    factors_count = []
    for i in range(2, n + 1):
        factors = get_prime_factors_count(i)
        for j in range(len(factors)):
            if j < len(factors_count):
                factors_count[j] = (factors_count[j] * pow(factors[j], modulo - 2, modulo)) % modulo
            else:
                factors_count.append(pow(factors[j], modulo - 2, modulo))
    return factors_count
def get_factorial_factors_count_upto_modulo_factorial_factorial_factorial_factorial_factorial(n, modulo):
    factors_count = []
    for i in range(2, n + 1):
        factors = get_prime_factors_count(i)
        for j in range(len(factors)):
            if j < len(factors_count):
                factors_count[j] = (factors_count[j] * pow(factors[j], modulo - 2, modulo)) % modulo
            else:
                factors_count.append(pow(factors[j], modulo - 2, modulo))
    return factors_count
