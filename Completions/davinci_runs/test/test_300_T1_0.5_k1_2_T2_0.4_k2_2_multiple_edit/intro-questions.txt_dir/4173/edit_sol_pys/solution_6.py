

import math

n, m = [int(x) for x in input().split()]

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

def get_prime_factors(x):
    factors = []
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0 and is_prime(i):
            factors.append(i)
    return factors

def get_prime_factor_count(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factor_count(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factor_count_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_prime_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_prime_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_prime_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_prime_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_prime_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_prime_factors_with_powers(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

def get_factors(x):
    factors = get_prime_factors(x)
    factor_count = {}
    for factor in factors:
        if factor not in factor_count:
            factor_count[factor] = 1
        else:
            factor_count[factor] += 1
    return factor_count

    min_bottles = n//2
    min_cost = min_bottles * b + (n%2)*a
    if a > b:
        min_cost = min(min_cost, (n//2)*a + (n%2)*b)
    
    print(min_cost)
