#!/usr/bin/env python3

# Recursive function for summing up the hailstone sequence
def hailstone_sum(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    elif n % 2 == 0:
        return n + hailstone_sum(n // 2)
    else:
        return n + hailstone_sum(3*n + 1)

if __name__ == "__main__":
    # Retrieve user input
    n = int(input())

print(hailstone_sum(n))
