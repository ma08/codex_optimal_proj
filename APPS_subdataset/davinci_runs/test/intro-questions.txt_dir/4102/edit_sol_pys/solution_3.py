#!/usr/bin/python3

# Read input.
n = int(input("Enter a number: "))

# Check if n is the sum of the cubes of its digits.
if (n == sum(int(digit)**3 for digit in str(n))):
    print("Yes, it is an armstrong number")
else:
    print("No, it is not an armstrong number")
