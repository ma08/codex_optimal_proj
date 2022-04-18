

# SOLUTION 2

# Get input
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

# Initialize variables
a_sum = sum(a)
b_sum = sum(b)
max_sum = max(a_sum, b_sum)
a_max = max(a)
b_max = max(b)
a_min = min(a)
b_min = min(b)

# Calculate results
if a_max > b_min:
    print(max_sum)
elif b_sum > a_sum:
    print(b_sum - a_sum)
else:
    print(a_sum - b_sum)

# Print result
print(max_sum)
