

# Read input
numbers = [int(x) for x in input().split()]

# Sort numbers
numbers.sort()

# Determine progression
progression = 0
if numbers[1] - numbers[0] == numbers[2] - numbers[1]:
    progression = numbers[1] - numbers[0]
else:
    progression = numbers[2] - numbers[1]

# Print missing number
print(numbers[2] + progression)
