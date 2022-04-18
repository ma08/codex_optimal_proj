

# This is a very simple problem, but I found it to be a good exercise to practice Python's string manipulation.

# Get input
a = input()
op = input()
b = input()

# Calculate result
if op == '+':
    result = str(int(a) + int(b))
elif op == '*':
    result = str(int(a) * int(b))

# Output result
print(result)
