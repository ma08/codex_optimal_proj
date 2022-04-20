import sys
import math
import heapq
import bisect
import random
import numpy as np
from collections import deque
from itertools import combinations, permutations
sys.setrecursionlimit(10**9)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inp_list(): return list(map(int, sys.stdin.readline().split()))
def lcm(x, y): return (x * y) // gcd(x, y)
def gcd(x, y): return x if y == 0 else gcd(y, x % y)
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(pow(n, 0.5))+1):
        if n % i == 0:
            return False
    return True
def eratosthenes_sieve(n):
    table = [0] * (n + 1)
    prime_list = []
    for i in range(2, n+1):
        if table[i] == 0:
            prime_list.append(i)
            for j in range(i + i, n + 1, i):
                table[j] = 1
    return prime_list
def prime_factorization(n):
    if n == 1: return []
    prime_list = eratosthenes_sieve(int(pow(n, 0.5))+1)
    prime_factor = []
    for prime in prime_list:
        if prime > n: break
        exponent = 0
        while n % prime == 0:
            exponent += 1
            n //= prime
        if exponent != 0:
            prime_factor.append([prime, exponent])
    if n != 1: prime_factor.append([n, 1])
    return prime_factor
def get_divisor(n):
    prime_factor = prime_factorization(n)
    divisor = []
    for prime, exponent in prime_factor:
        divisor.extend([prime**i for i in range(exponent + 1)])
    divisor.sort()
    return divisor
def get_digit(n):
    digit = []
    while n != 0:
        digit.append(n % 10)
        n //= 10
    return digit
def digit_sum(n):
    digit = get_digit(n)
    return sum(digit)
def digit_len(n):
    digit = get_digit(n)
    return len(digit)
def digit_count(n, k):
    digit = get_digit(n)
    return digit.count(k)
def digit_num(n, k):
    digit = get_digit(n)
    return digit.index(k)
def digit_to_num(digit):
    n = 0
    for d in digit:
        n = n * 10 + d
    return n
def is_permutation(n, m):
    digit_n = get_digit(n)
    digit_m = get_digit(m)
    return True if sorted(digit_n) == sorted(digit_m) else False
def is_palindrome(n):
    digit = get_digit(n)
    return True if digit == digit[::-1] else False
def is_pandigital(n, s=9):
    digit = get_digit(n)
    return len(digit) == s and not any(digit.count(d) != 1 for d in digit)
def is_pandigital_from_to(n, fr, to):
    digit = get_digit(n)
    return len(digit) == to - fr + 1 and not any(digit.count(d) != 1 for d in range(fr, to+1))
def is_pandigital_zero_to(n, to):
    digit = get_digit(n)
    return len(digit) == to and not any(digit.count(d) != 1 for d in range(to+1))
def is_pandigital_from(n, fr):
    digit = get_digit(n)
    return len(digit) == 9 and not any(digit.count(d) != 1 for d in range(1, fr+1))
def is_pandigital_zero_from(n, fr):
    digit = get_digit(n)
    return len(digit) == 10 and not any(digit.count(d) != 1 for d in range(fr, 10))
def is_pandigital_zero_to_from(n, to, fr):
    digit = get_digit(n)
    return len(digit) == to - fr + 1 and not any(digit.count(d) != 1 for d in range(fr, to+1))
def is_pandigital_zero_to_from_to(n, to1, fr1, to2, fr2):
    digit = get_digit(n)
    return len(digit) == to1 - fr1 + 1 + to2 - fr2 + 1 and not any(digit.count(d) != 1 for d in range(fr1, to1+1)) and not any(digit.count(d) != 1 for d in range(fr2, to2+1))
def is_narcissistic(n):
    digit = get_digit(n)
    n_digit = len(digit)
    return n == sum(d**n_digit for d in digit)
def is_smith(n):
    prime_factor = prime_factorization(n)
    digit_sum = 0
    for prime, exponent in prime_factor:
        digit_sum += sum(get_digit(prime)) * exponent
    return digit_sum == digit_sum(n)
def is_harshad(n):
    return n % digit_sum(n) == 0
def is_harshad_strong(n):
    return is_harshad(n) and is_prime(n // digit_sum(n))
def is_harshad_strong_right(n):
    digit = get_digit(n)
    for i in range(len(digit)):
        if not is_harshad_strong(digit_to_num(digit[i:])):
            return False
    return True
def is_harshad_strong_left(n):
    digit = get_digit(n)
    for i in range(len(digit)):
        if not is_harshad_strong(digit_to_num(digit[:i+1])):
            return False
    return True
def is_harshad_strong_both(n):
    return is_harshad_strong_right(n) and is_harshad_strong_left(n)
def is_polydivisible(n):
    digit = get_digit(n)
