

# Read the input
n = int(input())
divisors = [int(i) for i in input().split()]

# Initialize the numbers
x = 1
y = 1

# Calculate the numbers
for d in divisors:
    if d % x == 0:
        y *= d
    else:
        x *= d

# Print the result
print(x, y)