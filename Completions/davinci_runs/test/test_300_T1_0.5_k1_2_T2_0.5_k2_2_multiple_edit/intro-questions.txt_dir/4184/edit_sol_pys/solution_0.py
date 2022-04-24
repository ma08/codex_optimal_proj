

N = int(input())
weights = list(map(int, input().split()))

# Initialize minimum possible absolute difference to the sum of all weights
# (i.e. if we divide the weights into two groups with only one weight in each group)
min_diff = sum(weights)
first_group_sum = 0
for i in range(N):
    first_group_sum += weights[i]

    if i >= N - i - 1:
        diff = abs(first_group_sum - (sum(weights) - first_group_sum))
        if diff < min_diff:
            min_diff = diff
print(min_diff)
