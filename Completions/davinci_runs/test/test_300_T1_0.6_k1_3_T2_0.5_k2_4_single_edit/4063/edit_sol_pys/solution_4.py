import sys
import math


N = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))

# print(p)

# def is_prime(x):
#     if x == 2:
#         return True
#     elif x == 1 or x % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(math.sqrt(x)) + 1, 2):
#             if x % i == 0:
#                 return False
#     return True


def is_prime(x):
    if x == 2:
        return True
    if x == 1 or x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


for i in p:
    if is_prime(i):
        print('Prime')
    else:
        print('Not Prime')
