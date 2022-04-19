

# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# # find the minimum value in the array
# min_val = min(a)

# # find the number of times we need to divide by 2 to get to k
# num_divs = 0
# while min_val > k:
#     min_val //= 2
#     num_divs += 1

# print(num_divs)


# def sum_digits(n):
#     s = 0
#     while n:
#         s += n % 10
#         n //= 10
#     return s


# def sum_digits(n):
#     return sum(map(int, str(n)))


# print(sum_digits(2**1000))


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# def is_prime(n):
#     return n > 1 and all(n % i for i in range(2, n))


# def is_prime(n):
#     return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


# print(is_prime(2))


# def is_palindrome(s):
#     return s == s[::-1]


# print(is_palindrome("racecar"))


# def is_pangram(s):
#     return set("abcdefghijklmnopqrstuvwxyz") <= set(s.lower())


# print(is_pangram("The quick brown fox jumps over the lazy dog"))


# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b


# for i in fibonacci(10):
#     print(i)


# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(5))


# def factorial(n):
#     return 1 if n <= 1 else n * factorial(n - 1)


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))


# print(factorial(5))


# def factorial(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))
