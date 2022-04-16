import sys
import math

sys.setrecursionlimit(1000000)


def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)


def get_lcm(a, b):
    return int(a * b / get_gcd(a, b))


def solve(a, b):
    if a == b:
        return 1
    elif a < b:
        return 0
    else:
        cnt = 0
        for i in range(1, int(math.sqrt(a)) + 1):
            if a % i == 0:
                if a // i == i:
                    if i % b == 0:
                        cnt += 1
                else:
                    if i % b == 0:
                        cnt += 1
                    if a // i % b == 0:
                        cnt += 1
        return cnt


# a, b = map(int, input().split())
# print(solve(a, b))


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# n = int(input())
# print(is_prime(n))


def get_prime_divisor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


# n = int(input())
# print(get_prime_divisor(n))


def get_prime_factors(n):
    result = []
    while n > 1:
        result.append(get_prime_divisor(n))
        n //= get_prime_divisor(n)
    return result


# n = int(input())
# print(get_prime_factors(n))


def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return sorted(divisors)


# n = int(input())
# print(get_divisors(n))


def get_divisor_count(n):
    return len(get_divisors(n))


# n = int(input())
# print(get_divisor_count(n))


def get_divisor_sum(n):
    return sum(get_divisors(n))


# n = int(input())
# print(get_divisor_sum(n))


def get_divisor_pairs(n):
    divisors = get_divisors(n)
    pairs = []
    for i in range(len(divisors)):
        for j in range(i, len(divisors)):
            if divisors[i] * divisors[j] == n:
                pairs.append((divisors[i], divisors[j]))
    return pairs


# n = int(input())
# print(get_divisor_pairs(n))


def get_prime_factorization(n):
    factors = []
    while n > 1:
        factor = get_prime_divisor(n)
        factors.append(factor)
        n //= factor
    return factors


# n = int(input())
# print(get_prime_factorization(n))


def get_prime_factor_count(n):
    return len(get_prime_factorization(n))


# n = int(input())
# print(get_prime_factor_count(n))


def get_prime_factor_sum(n):
    return sum(get_prime_factorization(n))


# n = int(input())
# print(get_prime_factor_sum(n))


def get_prime_factor_pairs(n):
    factors = get_prime_factorization(n)
    pairs = []
    for i in range(len(factors)):
        for j in range(i, len(factors)):
            if factors[i] * factors[j] == n:
                pairs.append((factors[i], factors[j]))
    return pairs


# n = int(input())
# print(get_prime_factor_pairs(n))


def get_perfect_number(n):
    if n == get_divisor_sum(n):
        return True
    return False


# n = int(input())
# print(get_perfect_number(n))


def get_abundant_number(n):
    if n < get_divisor_sum(n):
        return True
    return False


# n = int(input())
# print(get_abundant_number(n))


def get_deficient_number(n):
    if n > get_divisor_sum(n):
        return True
    return False


# n = int(input())
# print(get_deficient_number(n))


def get_amicable_number(n):
    d1 = get_divisor_sum(n)
    d2 = get_divisor_sum(d1)
    if d1 != d2 and n == d2:
        return True
    return False


# n = int(input())
# print(get_amicable_number(n))


def get_sigma(n):
    return get_divisor_sum(n)


# n = int(input())
# print(get_sigma(n))


def get_tau(n):
    return get_prime_factor_count(n)


# n = int(input())
# print(get_tau(n))


def get_phi(n):
    factors = get_prime_factorization(n)
    result = n
    for factor in factors:
        result *= (1 - 1 / factor)
    return result


# n = int(input())
# print(get_phi(n))


def get_omega(n):
    return get_prime_factor_count(n)


r, c = map(int, input().split())
parking = [input() for _ in range(r)]

squash = [0, 0, 0, 0, 0]
for i in range(r-1):
    for j in range(c-1):
        if parking[i][j] == "#":
            continue
        elif parking[i][j] == ".":
            if parking[i+1][j] == "X" and parking[i][j+1] == "X" and parking[i+1][j+1] == "X":
                squash[4] += 1
            elif parking[i+1][j] == "X" and parking[i][j+1] == "X":
                squash[3] += 1
            elif parking[i+1][j] == "X" and parking[i+1][j+1] == "X":
                squash[3] += 1
            elif parking[i][j+1] == "X" and parking[i+1][j+1] == "X":
                squash[3] += 1
            elif parking[i+1][j] == "X":
                squash[2] += 1
            elif parking[i][j+1] == "X":
                squash[2] += 1
            elif parking[i+1][j+1] == "X":
                squash[2] += 1
            else:
                squash[0] += 1
        else:
            squash[1] += 1

print(squash[0])
print(squash[1])
print(squash[2])
print(squash[3])
print(squash[4])
