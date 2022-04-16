
# Define recursively defined hailstone sequence generator
def hailstone(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + hailstone(n // 2)
    else:
        return [n] + hailstone(3 * n + 1)

# Read input and print sum of hailstone sequence
n = int(input())
print(sum(hailstone(n)))
