

# SOLUTION
n, m, k = map(int, input().split())

# create an array to store the maximum sum of the numbers in each row
# in the range of [0, k-1]
max_sum = [0] * k

# for each row
for i in range(n):
    # create an array to store the sum of the numbers in the range of [0, k-1]
    sum_array = [0] * k
    # for each column
    for j in range(m):
        # read the number
        number = int(input())
        # calculate the sum of the numbers in the range of [0, k-1]
        # by the formula: sum_array[l] = sum(a[i][j] % k == l)
        sum_array[number % k] += 1
    # calculate the maximum sum of the numbers in the range of [0, k-1]
    # by the formula: max_sum[l] = max(max_sum[l], sum(a[i][j] % k == l))
    for l in range(k):
        max_sum[l] = max(max_sum[l], sum_array[l])

# calculate the sum of the maximum sum of the numbers in the range of [0, k-1]
# by the formula: sum_array[l] = max_sum[l] * l
sum_array = [0] * k
for l in range(k):
    sum_array[l] = max_sum[l] * l

# calculate the maximum sum of the numbers in the range of [0, k-1]
# by the formula: max_sum[l] = max(max_sum[l-1], sum_array[l])
for l in range(1, k):
    max_sum[l] = max(max_sum[l-1], sum_array[l])

# print the maximum sum of the numbers in the range of [0, k-1]
print(max_sum[k-1])