

# The sum of the three integers
sum = 0

# Read the three integers
for i in range(3):
    sum += int(input())

# Print the result
if sum >= 22:
    print("bust")
else:
    print("win")