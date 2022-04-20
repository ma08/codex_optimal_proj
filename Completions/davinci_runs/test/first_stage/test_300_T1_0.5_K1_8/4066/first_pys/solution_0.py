

# Read the input
n = int(input())
a = list(map(int, input().split()))

# Initialize the minimum lcm to be the lcm of the first two elements
min_lcm = lcm(a[0], a[1])

# Initialize the indices of the minimum lcm to be the first two elements
min_lcm_i = 0
min_lcm_j = 1

# Iterate over the rest of the array
for i in range(n):
    for j in range(i+1, n):
        # Check if the lcm of the two elements is smaller than the current minimum
        # If so, update the minimum lcm and the indices
        if lcm(a[i], a[j]) < min_lcm:
            min_lcm = lcm(a[i], a[j])
            min_lcm_i = i
            min_lcm_j = j

# Print the indices of the minimum lcm
print(min_lcm_i+1, min_lcm_j+1)