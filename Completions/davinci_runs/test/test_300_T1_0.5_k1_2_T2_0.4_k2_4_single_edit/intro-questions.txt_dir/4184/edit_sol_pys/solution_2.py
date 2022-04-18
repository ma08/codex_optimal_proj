

N = int(input())
weights = list(map(int, input().split()))

# Initialize minimum possible absolute difference to the sum of all weights
# (i.e. if we divide the weights into two groups with only one weight in each group)
min_diff = sum(weights)

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
