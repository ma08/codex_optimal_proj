
# Get input
a, b = map(int, input().split())

# Calculate max sum
if a > b:
    print(a + (a - 1))
else:
    print(b + (b - 1))
