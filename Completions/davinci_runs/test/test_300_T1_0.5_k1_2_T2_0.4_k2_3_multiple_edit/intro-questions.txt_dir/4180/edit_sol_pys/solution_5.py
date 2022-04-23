

# Read the input
N = int(input()) 
 
# Calculate the number of 500-yen bills required 
num_500_yen_bills = N // 500 
 
# Calculate the change 
change = N % 500 
 
# Print the change 
print(change) 
