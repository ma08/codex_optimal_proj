

# Read input file
with open('input.txt') as f:
    a = int(f.readline())
    op = f.readline().strip()
    b = int(f.readline())

# Calculate result
if op == '+':
    result = a + b
elif op == '*':
    result = a * b

# Print result to output file
with open('output.txt', 'w') as f:
    f.write(str(result))
