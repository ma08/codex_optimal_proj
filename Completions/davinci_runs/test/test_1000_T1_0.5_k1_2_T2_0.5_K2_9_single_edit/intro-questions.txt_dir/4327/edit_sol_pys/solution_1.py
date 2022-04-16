
# Receive input
a, p = map(int, input().split())

# Calculate the maximum number of apple pies we can make with what we have now
apple_pies = a*3 + p//2

# Print the result
print(apple_pies)
