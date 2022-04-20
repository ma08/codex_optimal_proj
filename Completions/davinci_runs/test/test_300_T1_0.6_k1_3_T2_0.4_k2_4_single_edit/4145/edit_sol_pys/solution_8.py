#!/usr/bin/env python3

import math

def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

x = int(input("Enter a number: "))

while True:
    if is_prime(x):
        print(x)
        break
    x += 1
