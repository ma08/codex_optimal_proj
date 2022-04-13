#!/usr/bin/env python3

# Recursive function for summing up hailstorm sequence
def hailstone_sum(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    elif n % 2 == 0:
        return n + hailstone_sum(n // 2)
    else:
        return n + hailstone_sum(3*n + 1)

# Retrieve user input
n = int(input())

print(hailstone_sum(n))
