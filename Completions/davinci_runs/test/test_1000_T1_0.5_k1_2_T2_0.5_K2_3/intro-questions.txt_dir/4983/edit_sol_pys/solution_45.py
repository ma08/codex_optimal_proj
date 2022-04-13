

# x = int(input())

# def product(x):
#     if x < 10:
#         return x
#     else:
#         y = 1
#         for i in str(x):
#             if int(i) != 0:
#                 y *= int(i)
#         return product(y)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))

# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(int(n / 10))

# print(sum_of_digits(1234))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(int(n / 10))

# print(sum_of_digits(1234))

# def to_digits(n):
#     lst = []
#     while n != 0:
#         digit = n % 10
#         lst = [digit] + lst
#         n = n // 10
#     return lst

# print(to_digits(123))

# def to_number(digits):
#     number = 0
#     for digit in digits:
#         number = number * 10 + digit
#     return number

# print(to_number([1, 2, 3]))

# def count_vowels(str):
#     count = 0
#     vowels = "aeiouy"
#     for i in str:
#         if i in vowels:
#             count += 1
#     return count

# print(count_vowels("Python"))

# def count_consonants(str):
#     count = 0
#     consonants = "bcdfghjklmnpqrstvwxz"
#     for i in str:
#         if i in consonants:
#             count += 1
#     return count

# print(count_consonants("Python"))

# def prime_number(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print(prime_number(5))

# def prime_numbers(n):
#     lst = []
#     for i in range(n):
#         if prime_number(i):
#             lst = lst + [i]
#     return lst

# print(prime_numbers(20))

# def fact_digits(n):
#     sum = 0
#     while n != 0:
#         digit = n % 10
#         sum += factorial(digit)
#         n = n // 10
#     return sum

# print(fact_digits(145))

# def palindrome(obj):
#     return str(obj) == str(obj)[::-1]

# print(palindrome("kapak"))
# print(palindrome(12321))
# print(palindrome("baba"))

# def char_histogram(string):
#     histogram = {}
#     for ch in string:
#         if ch not in histogram:
#             histogram[ch] = 1
#         else:
#             histogram[ch] += 1
#     return histogram

# print(char_histogram("Python!"))

# def p_score(n):
#     if palindrome(n):
#         return 1
#     else:
#         return 1 + p_score(n + int(str(n)[::-1]))

# print(p_score(121))

# def is_increasing(seq):
#     for i in range(len(seq) - 1):
#         if seq[i] >= seq[i + 1]:
#             return False
#     return True

# print(is_increasing([1, 2, 3, 4, 5]))

# def is_decreasing(seq):
#     for i in range(len(seq) - 1):
#         if seq[i] <= seq[i + 1]:
#             return False
#     return True

# print(is_decreasing([5, 4, 3, 2, 1]))

# def is_hack(n):
#     binary_num = bin(n)[2:]
#     if palindrome(binary_num) and n % 2 == 1:
#         return True
#     else:
#         return False

# print(is_hack(21))

# def next_hack(n):
#     n += 1
#     while not is_hack(n):
#         n += 1
#     return n

# print(next_hack(10))

# def sum_of_digits(n):
#     sum = 0
#     while n != 0:
#         digit = n % 10
#         sum += digit
#         n = n // 10
#     return sum

# def sum_of_digits_recursive(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits_recursive(n // 10)

# print(sum_of_digits_recursive(1234))

# def to_digits(n):
#     lst = []
#     while n != 0:
#         digit = n % 10
#         lst = [digit] + lst
#         n = n // 10
#     return lst

# def to_digits_recursive(n):
#     if n == 0:
#         return []
#     else:
#         return to_digits_recursive(n // 10) + [n % 10]

# print(to_digits_recursive(12345))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# def fact_digits(n):
#     sum = 0
#     while n != 0:
#         digit = n % 10
#         sum += factorial(digit)
#         n = n // 10
#     return sum

# print(fact_digits(145))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# def fact_digits(n):
#     sum = 0
#     while n != 0:
#         digit = n % 10
#         sum += factorial(digit)
#         n = n // 10
#     return sum

# print(fact_digits(145))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

#
# print(product(x))
