
# Read input from user
a = input("Enter a number: ")
op = input("Enter an operation: ")
b = input("Enter another number: ")

# Convert to ints
a = int(a)
b = int(b)

# Perform operation
if op == '+':
    print("Result: " + str(a + b))
elif op == '*':
    print("Result: " + str(a * b))
