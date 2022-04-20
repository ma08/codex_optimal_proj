
# Get input
a1, a2, a3 = map(int, input().split())  # Get input

# Print result
if a1 + a2 + a3 >= 22:  # Check if sum is greater than 22
    print("bust")  # Print result
else:
    print("win")
