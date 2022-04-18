#!/usr/bin/python3

# This is a very simple problem, but I found it to be a good exercise to practice Python's string manipulation.

# Get input.
a = int(input())
op = str(input())
b = int(input())

# Calculate result.
if op == '+':
    result = a + b
elif op == '*':
    result = a * b

# Output result.
print(result)
