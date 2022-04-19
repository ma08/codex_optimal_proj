
import math

n = int(input())

# Initialize minimum possible absolute difference to the sum of all numbers
# (i.e. if we divide the numbers into two groups with only one number in each group).
min_diff = sum(numbers)

# Initialize the sum of the numbers in the first group to 0.
first_group_sum = 0.0

# Loop through the numbers from the smallest to the largest.
for i in range(n):
    # Increment the sum of the numbers in the first group by the number indexed i.
    first_group_sum += numbers[i]

    # If the number of numbers in the first group is greater than or equal to
    # the number of numbers in the second group, calculate the difference between
    # the sum of the numbers in the first group and the sum of the numbers in the second group.
    if i >= n - i - 1:
        # Calculate the difference between the sum of the numbers in the first group and
        # the sum of the numbers in the second group, and update the minimum possible absolute difference.
        diff = abs(first_group_sum - (sum(numbers) - first_group_sum))
        if diff < min_diff:
            min_diff = diff

# Print the minimum possible absolute difference, rounded to 1 decimal place.
print(round(min_diff, 1))
