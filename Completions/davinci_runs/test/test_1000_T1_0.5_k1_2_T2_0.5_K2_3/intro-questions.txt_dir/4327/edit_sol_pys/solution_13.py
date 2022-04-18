
A, P = map(int, input().split())

# Calculate the maximum number of apple pies we can make with what we have now
apple_pies = A*3 + P//2 # A*3 because we need 3 apples for one pie and P//2 because we need 2 pastry for one pie

# Print the result
print(apple_pies)
