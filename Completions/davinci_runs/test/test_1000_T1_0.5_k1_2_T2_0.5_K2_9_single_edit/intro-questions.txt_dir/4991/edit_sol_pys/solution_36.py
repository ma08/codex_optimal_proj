
# Define recursively defined hailstone sequence generator
def hailstone(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return n + hailstone(n // 2)
    else:
        return n + hailstone(3 * n + 1)

# Read input
n = int(input())

# Print sum of hailstone sequence
print(hailstone(n))
