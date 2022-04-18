
#
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     if n < k:
#         print(1)
#     else:
#         print(n // k + n % k)


# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)
#
#
# print(sum_of_digits(12345))
#
#
# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)
#
#
# print(sum_of_digits(12345))


# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)
#
#
# print(sum_of_digits(12345))


# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)
#
#
# print(sum_of_digits(12345))


def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(12345))
