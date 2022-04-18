
# Get input
n = int(input())
a = [int(input()) for i in range(n)]

# Calculate the maximum number of candies that can be eaten
max_num_candies = 0
for i in range(2**n):
    num_candies = 0
    for j in range(n):
        if ((i >> j) & 1):
            num_candies += a[j]
    if num_candies > max_num_candies:
        max_num_candies = num_candies

print(max_num_candies)
