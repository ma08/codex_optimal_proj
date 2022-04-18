

N = int(input())
weights = list(map(int, input().split()))

# Initialize the sum of the weights in the first group to 0.
first_group_sum = weights[0]

# Initialize the sum of the weights in the second group to 0.
second_group_sum = 0

# Loop through the weights from the smallest to the largest.
for i in range(1, N):
    # Increment the sum of the weights in the second group by the weight indexed i - 1.
    second_group_sum += weights[i - 1]

    # Increment the sum of the weights in the first group by the weight indexed i.
    # the number of weights in the second group, calculate the difference between
    # the sum of the weights in the first group and the sum of the weights in the second group.
    if i >= N - i:
        # Calculate the difference between the sum of the weights in the first group and
        # the sum of the weights in the second group, and update the minimum possible absolute difference.
        diff = abs(first_group_sum - second_group_sum)
        if diff < min_diff:
            min_diff = diff

    # Increment the sum of the weights in the first group by the weight indexed i.
    first_group_sum += weights[i]

# Print the minimum possible absolute difference.
print(min_diff)
