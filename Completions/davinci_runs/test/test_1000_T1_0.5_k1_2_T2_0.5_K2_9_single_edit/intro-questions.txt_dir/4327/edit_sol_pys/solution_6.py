

# Receive input
A, P = map(int, input().split())

# Calculate the maximum number of apple pies we can make with what we have now
apple_pies = A * 3 + P // 2

# Print the result
print(apple_pies)
