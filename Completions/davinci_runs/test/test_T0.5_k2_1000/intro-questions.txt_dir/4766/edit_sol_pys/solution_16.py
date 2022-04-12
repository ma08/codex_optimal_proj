def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = [2]
    for i in range(3, n, 2):
        if is_prime(i):
            primes.append(i)
    return primes

def get_prime_factors(n):
    prime_factors = []
    primes = get_primes(n)
    for prime in primes:
        if n % prime == 0:
            prime_factors.append(prime)
    return prime_factors

def get_prime_factor_counts(n):
    prime_factors = get_prime_factors(n)
    prime_factor_counts = []
    for prime in prime_factors:
        count = 0
        while n % prime == 0:
            count += 1
            n = n / prime
        prime_factor_counts.append(count)
    return prime_factor_counts

def get_prime_factor_count(n):
    prime_factor_counts = get_prime_factor_counts(n)
    prime_factor_count = 1
    for count in prime_factor_counts:
        prime_factor_count *= (count + 1)
    return prime_factor_count

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n / i:
                divisors.append(n / i)
    return divisors

def get_divisor_count(n):
    return len(get_divisors(n))

def get_triangle_number(n):
    return n * (n + 1) / 2

def is_triangle_number(n):
    return (1 + (1 + 8 * n)**0.5) / 2 % 1 == 0

def get_pentagonal_number(n):
    return n * (3 * n - 1) / 2

def is_pentagonal_number(n):
    return (1 + (1 + 24 * n)**0.5) / 6 % 1 == 0

def get_hexagonal_number(n):
    return n * (2 * n - 1)

def is_hexagonal_number(n):
    return (1 + (1 + 8 * n)**0.5) / 4 % 1 == 0

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def get_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def get_combination(n, r):
    return get_factorial(n) / (get_factorial(r) * get_factorial(n - r))

def get_permutation(n, r):
    return get_factorial(n) / get_factorial(n - r)

def get_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n + 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci

def get_fibonacci_number(n):
    return get_fibonacci(n)[-1]

def is_fibonacci_number(n):
    return (5 * n**2 + 4)**0.5 % 1 == 0 or (5 * n**2 - 4)**0.5 % 1 == 0

def get_pythagorean_triples(n):
    triples = []
    for a in range(1, n):
        for b in range(a, n):
            c = (a**2 + b**2)**0.5
            if c % 1 == 0 and c <= n:
                triples.append((a, b, int(c)))
    return triples

def get_pythagorean_triple_perimeters(n):
    perimeters = []
    for triple in get_pythagorean_triples(n):
        perimeter = sum(triple)
        if perimeter <= n:
            perimeters.append(perimeter)
    return perimeters

def get_pythagorean_triple_perimeter_counts(n):
    perimeters = get_pythagorean_triple_perimeters(n)
    perimeter_counts = []
    for i in range(n + 1):
        perimeter_counts.append(perimeters.count(i))
    return perimeter_counts

def get_pythagorean_triple_perimeter_count(n):
    return get_pythagorean_triple_perimeter_counts(n).count(max(get_pythagorean_triple_perimeter_counts(n)))

def get_pythagorean_triple_perimeter_max(n):
    return get_pythagorean_triple_perimeter_counts(n).index(max(get_pythagorean_triple_perimeter_counts(n)))
