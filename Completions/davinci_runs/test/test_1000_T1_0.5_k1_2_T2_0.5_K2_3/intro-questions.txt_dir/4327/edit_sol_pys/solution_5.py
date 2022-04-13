

# Receive input from STDIN
a, p = map(int, input().split())

# Calculate the maximum number of apple pies we can make with what we have
apple_pies = a*3 + p//2

# Print the result
print(apple_pies)
