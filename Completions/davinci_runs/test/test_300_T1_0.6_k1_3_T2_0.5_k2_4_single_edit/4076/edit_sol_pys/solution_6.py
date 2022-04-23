

import sys
import math

# def distanceBetweenHands(hour, minute):
#     hour *= 30.0
#     minute *= 6.0

#     x1 = 3.0 * math.cos(math.radians(hour))
#     y1 = 3.0 * math.sin(math.radians(hour))
#     x2 = 4.0 * math.cos(math.radians(minute))
#     y2 = 4.0 * math.sin(math.radians(minute))

#     return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

# params = sys.stdin.readline().split()
# a = int(params[0])
# b = int(params[1])
# h = int(params[2])
# m = int(params[3])

# print(distanceBetweenHands(h, m))


def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def countPrimes(a, b):
    count = 0
    for i in range(a, b + 1):
        if isPrime(i):
            count += 1
    return count


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
print(countPrimes(a, b))
