

# Read input from stdin
numbers = [int(x) for x in input().split()] # list of three numbers

# Sort numbers in ascending order
numbers.sort()

# Determine progression step (difference between two consecutive numbers)
step = 0
if numbers[1] - numbers[0] == numbers[2] - numbers[1]: # arithmetic progression (equal step)
	step = numbers[1] - numbers[0]
else: # geometric progression (unequal step)
	step = numbers[2] - numbers[1]

# Print missing number
print(numbers[2] + step)
