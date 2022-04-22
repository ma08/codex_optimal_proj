

N = int(input())
weights = list(map(int, input().split()))

# Initialize the sum of the weights in the first group to 0.
first_group_sum = weights[0]

# Loop through the weights from the second smallest to the largest.
for i in range(1, N):
    # If the sum of the weights in the first group is less than or equal to
    # the sum of the weights in the second group, increment the sum of the
    # weights in the first group by the weight indexed i.
    if first_group_sum <= sum(weights) - first_group_sum:
        first_group_sum += weights[i]
