

N = int(input())
weights = list(map(int, input().split()))

# Initialize the sum of the weights in the first group to 0.
first_group_sum = sum(weights)

# Initialize the sum of the weights in the second group to 0.
second_group_sum = 0

# Loop through the weights from the smallest to the largest.
for i in range(N):
    # Decrement the sum of the weights in the first group by the weight indexed i.
    first_group_sum -= weights[i]

    # Increment the sum of the weights in the second group by the weight indexed i.
    second_group_sum += weights[i]

    # If the number of weights in the first group is less than or equal to
    # the number of weights in the second group, calculate the absolute difference between
    # the sum of the weights in the first group and the sum of the weights in the second group.
    if i <= N - i - 1:
        # Calculate the absolute difference between the sum of the weights in the first group and
        # the sum of the weights in the second group, and update the minimum possible absolute difference.
        min_diff = min(min_diff, abs(first_group_sum - second_group_sum))

# Print the minimum possible absolute difference.
print(min_diff)
