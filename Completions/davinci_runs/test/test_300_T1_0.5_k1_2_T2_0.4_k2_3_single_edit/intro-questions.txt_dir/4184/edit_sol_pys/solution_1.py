
N = int(input())
a = list(map(int, input().split()))

# Initialize minimum possible absolute difference to the sum of all a
# (i.e. if we divide the a into two groups with only one a in each group).
min_diff = sum(a)

# Initialize the sum of the a in the first group to 0.
first_group_sum = 0 

# Loop through the a from the smallest to the largest.
for i in range(N):
    # Increment the sum of the a in the first group by the a indexed i.
    first_group_sum += a[i]

    # If the number of weights in the first group is greater than or equal to
    # the number of a in the second group, calculate the difference between
    # the sum of the a in the first group and the sum of the a in the second group.
    if i >= N - i - 1:
        # Calculate the difference between the sum of the a in the first group and
        # the sum of the a in the second group, and update the minimum possible absolute difference.
        diff = abs(first_group_sum - (sum(a) - first_group_sum))
        if diff < min_diff:
            min_diff = diff

# Print the minimum possible absolute difference.
print(min_diff)
