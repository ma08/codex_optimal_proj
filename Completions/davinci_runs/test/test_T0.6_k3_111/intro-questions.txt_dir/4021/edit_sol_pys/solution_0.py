
# Read input.
a = int(input())

# Find the number of 1's required.
num_ones = 0

# Keep going until a is 0.
while a > 0:
    # If a is even, add 1
    if a % 2 == 0:
        num_ones += 1
    # Otherwise, subtract 1
    else:
        num_ones -= 1
    # Divide by 2
    a //= 2

print(abs(num_ones))
