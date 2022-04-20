

# Get input
a, b, c = map(int, input().split())

# Calculate
if a - b >= c:
    print(c)
else:
    print(c - (a - b))