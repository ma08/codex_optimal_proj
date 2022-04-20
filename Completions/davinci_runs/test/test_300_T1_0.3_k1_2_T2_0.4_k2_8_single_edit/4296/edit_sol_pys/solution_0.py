
# Get input
a1, a2, a3 = map(int, input().split())  # Get input

# Print result
if a1 + a2 + a3 >= 22:  # If sum of input is 22 or more
    print("bust")  # Print "bust"
else:  # If sum of input is less than 22
    print("win")  # Print "win"
