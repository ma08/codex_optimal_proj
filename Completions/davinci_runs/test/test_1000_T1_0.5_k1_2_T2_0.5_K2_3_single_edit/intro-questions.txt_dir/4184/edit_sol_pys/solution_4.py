

N = int(input())
weights = list(map(int, input().split()))

weights.sort()
# Initialize the sum of the weights in the first group to the largest weight.
first_group_sum = weights[-1]

# Initialize the sum of the weights in the second group to the sum of all other weights.
second_group_sum = sum(weights[:-1])

# Initialize the minimum possible absolute difference to the difference between the two group sums.
min_diff = abs(first_group_sum - second_group_sum)

# Loop through the weights from the second largest to the smallest.
for i in range(N - 2, -1, -1):
    # Increment the sum of the weights in the first group by the weight indexed i,
    # and decrement the sum of the weights in the second group by the same weight.
    first_group_sum += weights[i]
    second_group_sum -= weights[i]

    # Calculate the difference between the sum of the weights in the first group and
    # the sum of the weights in the second group, and update the minimum possible absolute difference.
    diff = abs(first_group_sum - second_group_sum)
    if diff < min_diff:
        min_diff = diff

# Print the minimum possible absolute difference.
print(min_diff)
