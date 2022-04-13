

# Read input
numbers = [int(x) for x in input().split()]

# Sort numbers
numbers.sort()

# Determine progression and missing number
missing = 0 #
if numbers[1] - numbers[0] != numbers[2] - numbers[1]:
	missing = numbers[2] + numbers[1] - numbers[0]
else:
	missing = numbers[2] + numbers[2] - numbers[1]

# Print missing number
print(missing)
