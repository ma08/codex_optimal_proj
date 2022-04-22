

N = int(input())
weights = list(map(int, input().split()))

# Initialize the sum of the weights in the first group to 0.


def partition(weights, N, first_group_sum, total_sum):
    # If the number of weights in the first group is greater than or equal to
    # the number of weights in the second group, calculate the difference between
    # the sum of the weights in the first group and the sum of the weights in the second group.
    if N >= N - N - 1:
        # Calculate the difference between the sum of the weights in the first group and
        # the sum of the weights in the second group, and update the minimum possible absolute difference.
        diff = abs(first_group_sum - (total_sum - first_group_sum))
        if diff < min_diff:
            min_diff = diff
    return min_diff


# Loop through the weights from the smallest to the largest.
for i in range(N):
    # Increment the sum of the weights in the first group by the weight indexed i
    # total_sum = sum(weights)
    # first_group_sum = first_group_sum + weights[i]

    partition(weights, N, first_group_sum, total_sum)

# Print the minimum possible absolute difference.
print(min_diff)
