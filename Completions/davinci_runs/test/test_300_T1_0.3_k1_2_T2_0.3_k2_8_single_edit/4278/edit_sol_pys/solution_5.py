
import math
import sys

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_dict = {}
    s2_dict = {}
    for c in s1:
        if c not in s1_dict:
            s1_dict[c] = 1
        else:
            s1_dict[c] += 1
    for c in s2:
        if c not in s2_dict:
            s2_dict[c] = 1
        else:
            s2_dict[c] += 1
    return s1_dict == s2_dict
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_factors(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
                factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def get_prime_factors_dict(n):
    factors = {}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
                if i not in factors:
                    factors[i] = 1
                else:
                    factors[i] += 1
    if n > 1:
        if n not in factors:
            factors[n] = 1
        else:
            factors[n] += 1
    return factors

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return divisors

def get_divisors_dict(n):
    divisors = {}
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors[i] = 1
            if n // i != i:
                divisors[n // i] = 1
    return divisors

def get_divisors_count(n):
    divisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors += 1
            if n // i != i:
                divisors += 1
    return divisors

def get_divisors_count_dict(n):
    divisors = {}
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i not in divisors:
                divisors[i] = 1
            else:
                divisors[i] += 1
            if n // i != i:
                if n // i not in divisors:
                    divisors[n // i] = 1
                else:
                    divisors[n // i] += 1
    return divisors

def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    return a * b // get_gcd(a, b)

def get_gcd_list(numbers):
    gcd = numbers[0]
    for n in numbers:
        gcd = get_gcd(gcd, n)
    return gcd

def get_lcm_list(numbers):
    lcm = numbers[0]
    for n in numbers:
        lcm = get_lcm(lcm, n)
    return lcm

def get_gcd_dict(numbers):
    gcd = numbers[0]
    for n in numbers:
        gcd = get_gcd(gcd, n)
    return gcd

def get_lcm_dict(numbers):
    lcm = numbers[0]
    for n in numbers:
        lcm = get_lcm(lcm, n)
    return lcm

def get_gcd_dict(numbers):
    gcd = numbers[0]
    for n in numbers:
        gcd = get_gcd(gcd, n)
    return gcd

def get_lcm_dict(numbers):
    lcm = numbers[0]
    for n in numbers:
        lcm = get_lcm(lcm, n)
    return lcm

def get_gcd_dict(numbers):
    gcd = numbers[0]
    for n in numbers:
        gcd = get_gcd(gcd, n)
    return gcd

def get_lcm_dict(numbers):
    lcm = numbers[0]
    for n in numbers:
        lcm = get_lcm(lcm, n)
    return lcm

def get_gcd_dict(numbers):
    gcd = numbers[0]
    for n in numbers:
        gcd = get_gcd(gcd, n)
    return gcd

def get_lcm_dict(numbers):
    lcm = numbers[0]
    for n in numbers:
        lcm = get_lcm(lcm, n)
    return lcm

def get_gcd_dict(numbers):
    gcd = numbers[0]
    for n in numbers:
        gcd = get_gcd(gcd, n)
    return gcd

def get_lcm_dict(numbers):
    lcm = numbers[0]
    for n in numbers:
        lcm = get_lcm(lcm, n)
    return lcm

def get_gcd_dict(numbers):
    gcd = numbers[0]
    for n in numbers:
        gcd = get_gcd(gcd, n)
    return gcd

def get_lcm_dict(numbers):
    lcm = numbers[0]
    for n in numbers:
        lcm = get_lcm(lcm, n)
    return lcm

def get_gcd_dict(numbers):
    gcd = numbers[0]
    for n in numbers:
        gcd = get_gcd(gcd, n)
    return gcd

def get_lcm_dict(numbers):
    lcm = numbers[0]
    for n in numbers:
        lcm = get_lcm(lcm, n)
    return lcm



def main():
    n = int(sys.stdin.readline().rstrip())
    s = []
    for _ in range(n):
        s.append(sys.stdin.readline().rstrip())
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if is_anagram(s[i], s[j]):
                count += 1
    print(count)


if __name__ == '__main__':
    main()
