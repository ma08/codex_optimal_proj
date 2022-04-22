import sys
import math


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    numbers_list = [2]
    number = 3
    while len(numbers_list) < n:
        if is_prime(number):
            numbers_list.append(number)
        number += 2
    return numbers_list[-1]

print(nth_prime(10001))

# def nth_prime(n):
#     if n == 1:
#         return 2
#     if n == 2:
#         return 3
#     counter = 3
#     number = 5
#     while counter < n:
#         number += 2
#         if is_prime(number):
#             counter += 1
#     return number
#
# print(nth_prime(10001))

# def nth_prime(n):
#     if n == 1:
#         return 2
#     if n == 2:
#         return 3
#     counter = 2
#     number = 3
#     while counter < n:
#         number += 2
#         if is_prime(number):
#             counter += 1
#     return number
#
# print(nth_prime(10001))

# def nth_prime(n):
#     if n == 1:
#         return 2
#     if n == 2:
#         return 3
#     counter = 2
#     number = 3
#     while counter < n:
#         number += 2
#         if is_prime(number):
#             counter += 1
#     return number
#
# print(nth_prime(10001))
