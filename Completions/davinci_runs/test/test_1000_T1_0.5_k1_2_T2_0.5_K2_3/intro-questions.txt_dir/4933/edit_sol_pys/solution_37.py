
# Read input
numbers = [int(x) for x in input().split()]

# Sort numbers
numbers.sort()

# Determine progression step
step = 0
if numbers[1] - numbers[0] == numbers[2] - numbers[1]: # Arithmetic progression
	step = numbers[1] - numbers[0]
else:
	step = numbers[2] - numbers[1]

# Print missing number
print(numbers[2] + step)
