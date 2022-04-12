

# Receive input from the user
A, P = map(int, input().split()) # A = number of apples, P = number of pastry

# Calculate the maximum number of apple pies we can make with what we have now
apple_pies = A*3 + P//2

# Print the result
print(apple_pies)
