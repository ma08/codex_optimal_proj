

# Get the input from the user
A, B = map(float, input().split()) # split the input with space

# Compute A \times B, truncate its fractional part, and print the result as an integer
print(int(A * B))
