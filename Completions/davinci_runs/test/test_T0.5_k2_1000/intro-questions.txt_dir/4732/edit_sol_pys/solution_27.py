
# Read input from user
a = input("Enter first number: ")
op = input("Enter operation: ")
b = input("Enter second number: ")

# Convert to ints
a = int(a)
b = int(b)

# Perform operation
if op == '+':
    print(a + b)
elif op == '*':
    print(a * b)
