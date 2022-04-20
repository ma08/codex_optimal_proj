

# Read input and convert to int
num_1000_yen_bills = int(input())

# Calculate the number of 500-yen bills required
num_500_yen_bills = num_1000_yen_bills // 500

# Calculate the number of 100-yen bills required
num_100_yen_bills = num_1000_yen_bills % 500

# Print the change
print(change)
