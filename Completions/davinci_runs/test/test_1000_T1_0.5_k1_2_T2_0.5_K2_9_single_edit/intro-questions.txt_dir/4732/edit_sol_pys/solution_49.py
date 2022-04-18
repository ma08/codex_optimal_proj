

# Get input.
a = input()
op = input()
b = input()

# Calculate result.
if op == '+':
    result = str(int(a) + int(b))
elif op == '*':
    result = str(int(a) * int(b))

# Output result.
print(result)
