

# Get input
a, b = map(int, input().split()) # int(input())

# Calculate max coins
if a > b:
    print(a + (a - 1)) # print(a + (a - 1))
else:
    print(b + (b - 1)) # print(b + (b - 1))
