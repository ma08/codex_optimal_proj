
# Read input
N = int(input())

# Calculate the number of 500-yen coins required
num_500_yen_coins = N // 500

# Calculate the change
change = N % 1000

# Print the change
print(change)
