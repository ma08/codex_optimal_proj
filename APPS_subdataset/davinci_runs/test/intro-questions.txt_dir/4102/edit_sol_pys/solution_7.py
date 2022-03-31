
# Read input.
n = int(input())

# Check if n is the sum of the cubes of its digits.
if (n == sum(int(digit)**3 for digit in str(n))):
    print("Yes")
else:
    print("No")
