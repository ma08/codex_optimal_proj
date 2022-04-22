#!/bin/python3


import sys

def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        if grades[i] < 38:
            grades[i] = grades[i]
        elif grades[i] % 5 >= 3:
            grades[i] = grades[i] + (5 - (grades[i] % 5))
    return grades

# Initialize the sum of the weights in the first group to 0.
first_group_sum = 0

# Loop through the weights from the smallest to the largest.
for i in range(N):
    # Increment the sum of the weights in the first group by the weight indexed i.
    first_group_sum += weights[i]

    # If the number of weights in the first group is greater than or equal to
    # the number of weights in the second group, calculate the difference between
    # the sum of the weights in the first group and the sum of the weights in the second group.
    if i >= N - i - 1:
        # Calculate the difference between the sum of the weights in the first group and
        # the sum of the weights in the second group, and update the minimum possible absolute difference.
        diff = abs(first_group_sum - (sum(weights) - first_group_sum))
        if diff < min_diff:
            min_diff = diff

# Print the minimum possible absolute difference.
print(min_diff)
