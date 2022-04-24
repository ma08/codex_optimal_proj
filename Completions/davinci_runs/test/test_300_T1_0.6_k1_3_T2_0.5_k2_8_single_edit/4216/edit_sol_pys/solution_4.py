

# import math

# n = int(input())

# primes = []
# for i in range(2, int(math.sqrt(n))):
#     if n % i == 0:
#         primes.append(i)

# print(n // primes[0])


# def is_prime(n):
#     if n == 1:
#         return False
#     for k in range(2, int(n**0.5) + 1):
#         if n % k == 0:
#             return False
#     return True


# def main():
#     n = int(input())
#     if not is_prime(n):
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 print(n // i)
#                 break
#     else:
#         print(1)


# if __name__ == '__main__':
#     main()


def main():
    n = int(input())
    if n % 2 == 0:
        print(n // 2)
    else:
        print(n)


if __name__ == '__main__':
    main()
