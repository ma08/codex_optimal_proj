

import math
import sys

# get input
inputList = sys.stdin.readline().rstrip('\n').split()

# convert to integer
A = int(inputList[0])
B = int(inputList[1])
K = int(inputList[2])

# get the number of common divisors
commonDivisors = math.gcd(A, B)

# get the list of common divisors
divisorsList = []
for i in range(1, commonDivisors+1):
    if commonDivisors % i == 0:
        divisorsList.append(i)

# print the K-th largest common divisor
print(divisorsList[K-1])