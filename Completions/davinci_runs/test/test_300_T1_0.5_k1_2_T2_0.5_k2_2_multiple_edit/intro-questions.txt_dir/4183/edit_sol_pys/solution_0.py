import math

def gcd_f(a, b):
    if b == 0:
        return a
    return gcd_f(b, a%b)

n = int(input()) # number of numbers
t = list(map(int, input().split())) # numbers

gcd = t[0]
for i in range(1, n):
    gcd = gcd_f(gcd, t[i])

print(gcd)

# printing the prime numbers
# def isPrime(n):
#     if n == 2:
#         return True
#     if n < 2 or n%2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(n))+1, 2):
#         if n%i == 0:
#             return False
#     return True

# for i in range(2, 100):
#     if isPrime(i):
#         print(i, end=" ")

# print()

# printing the prime numbers
# def isPrime(n):
#     if n == 2:
#         return True
#     if n < 2 or n%2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(n))+1, 2):
#         if n%i == 0:
#             return False
#     return True

# for i in range(2, 100):
#     if isPrime(i):
#         print(i, end=" ")

# print()

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# for i in range(10):
#     print(fib(i), end=" ")

# print()

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# for i in range(10):
#     print(fib(i), end=" ")

# print()

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i), end=" ")

print()
