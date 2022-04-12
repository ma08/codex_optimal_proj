
# Define recursively defined hailstorm sequence generator
def hailstone(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + hailstone(n // 2)
    else:
        return [n] + hailstone(3 * n + 1)

# Read input
n = int(input())

# Print sum of hailstorm sequence
print(sum(hailstone(n)))
