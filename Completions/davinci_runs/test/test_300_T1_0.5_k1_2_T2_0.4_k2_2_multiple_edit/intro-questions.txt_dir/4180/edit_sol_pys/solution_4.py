

# Read input
N = int(input())

# Calculate the number of 100-yen coins required
num_100_yen_coins = N // 100

# Calculate the change
change = N % 100

# Print the change
print(change)
