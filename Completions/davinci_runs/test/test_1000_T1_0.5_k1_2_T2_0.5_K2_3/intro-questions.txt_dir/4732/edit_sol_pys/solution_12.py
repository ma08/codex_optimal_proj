
# Read input
a = input("Please enter your first number: ")
op = input("Please enter your operation: ")
b = input("Please enter your second number: ")

# Convert to ints
a = int(a)
b = int(b)

# Perform operation
if op == '+':
    print(a + b)
elif op == '*':
    print(a * b)
