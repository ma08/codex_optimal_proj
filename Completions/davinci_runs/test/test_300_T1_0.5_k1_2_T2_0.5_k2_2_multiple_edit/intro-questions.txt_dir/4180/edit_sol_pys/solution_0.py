

# Read input
N = int(input())

# Calculate the number of 500-yen coins required
num_500_yen_coins = N // 500

# Calculate the number of 100-yen coins required to make up the change
num_100_yen_coins = (N - num_500_yen_coins * 500) // 100

# Calculate the change
change = N % 1000

# Print the change
print(change)
