

# Read the input
N = int(input()) # the number of yen coins

# Calculate the number of 500-yen coins required
num_500_yen_coins = N // 500

# Calculate the change
change = N % 500

# Print the change
print(change)
