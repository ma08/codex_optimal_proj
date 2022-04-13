# # input

# s = input()
# # output

# result = ""

# for char in s:
#     if char == "0":
#         result += "0"
#     elif char == "1":
#         result += "1"
#     else:
#         result = result[:-1]

# print(result)


# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True


# n = int(input())
# for i in range(1, n + 1):
#     if is_prime(i):
#         print(i)


# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True


# def get_primes(n):
#     primes = []
#     for i in range(1, n + 1):
#         if is_prime(i):
#             primes.append(i)
#     return primes


# n = int(input())
# for p in get_primes(n):
#     print(p)


# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True


# def get_primes(n):
#     primes = []
#     for i in range(1, n + 1):
#         if is_prime(i):
#             primes.append(i)
#     return primes


# def get_prime_factors(n):
#     factors = []
#     for p in get_primes(n):
#         if n % p == 0:
#             factors.append(p)
#     return factors


# n = int(input())
# for f in get_prime_factors(n):
#     print(f)


# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True


# def get_primes(n):
#     primes = []
#     for i in range(1, n + 1):
#         if is_prime(i):
#             primes.append(i)
#     return primes


# def get_prime_factors(n):
#     factors = []
#     for p in get_primes(n):
#         if n % p == 0:
#             factors.append(p)
#     return factors


# def get_prime_factorization(n):
#     factors = []
#     for p in get_primes(n):
#         if n % p == 0:
#             factors.append(p)
#             n //= p
#     return factors


# n = int(input())
# for f in get_prime_factorization(n):
#     print(f)


# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True


# def get_primes(n):
#     primes = []
#     for i in range(1, n + 1):
#         if is_prime(i):
#             primes.append(i)
#     return primes


# def get_prime_factors(n):
#     factors = []
#     for p in get_primes(n):
#         if n % p == 0:
#             factors.append(p)
#     return factors


# def get_prime_factorization(n):
#     factors = []
#     for p in get_primes(n):
#         if n % p == 0:
#             factors.append(p)
#             n //= p
#     return factors


# def get_prime_factorization_with_count(n):
#     factors = []
#     for p in get_primes(n):
#         count = 0
#         while n % p == 0:
#             count += 1
#             n //= p
#         factors.append((p, count))
#     return factors


# n = int(input())
# for f in get_prime_factorization_with_count(n):
#     print(f)


# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True


# def get_primes(n):
#     primes = []
#     for i in range(1, n + 1):
#         if is_prime(i):
#             primes.append(i)
#     return primes


# def get_prime_factors(n):
#     factors = []
#     for p in get_primes(n):
#         if n % p == 0:
#             factors.append(p)
#     return factors


# def get_prime_factorization(n):
#     factors = []
#     for p in get_primes(n):
#         if n % p == 0:
#             factors.append(p)
#             n //= p
#     return factors


# def get_prime_factorization_with_count(n):
#     factors = []
#     for p in get_primes(n):
#         count = 0
#         while n % p == 0:
#             count += 1
#             n //= p
#         factors.append((p, count))
#     return factors


# n = int(input())
# for p, c in get_prime_factorization_with_count(n):
#     print(p, c)
