

# Define recursively hailstone sequence generator
def hailstone(n):
    if n == 1:
        return [1]
    if n % 2 == 0:
        return [n] + hailstone(n // 2)
    return [n] + hailstone(3 * n + 1)

# Read input
n = int(input())

# Print sum of hailstone sequence
print(sum(hailstone(n)))
