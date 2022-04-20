
# Read input
N = int(input())

# Calculate the change
change = N % 1000 # N % 1000 = N - (N // 1000) * 1000

# Print the change
print(change)
