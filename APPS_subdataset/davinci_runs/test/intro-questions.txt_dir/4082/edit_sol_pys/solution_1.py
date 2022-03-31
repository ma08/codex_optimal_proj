

# SOLUTION

n = int(input())
a = list(map(int, input().split()))

# the maximum length of the decreasing subarray
max_length = 1
# the length of the decreasing subarray
length = 1

# iterate through the array
for i in range(1, n):
    # if the current element is greater than
    # the previous element, then increase
    # the length of the decreasing subarray
    if a[i] > a[i - 1]:
        length += 1
    else:
        # if the current element is not greater than
        # the previous element, then update the maximum length
        # of the decreasing subarray
        max_length = max(max_length, length)
        # reset the length of the decreasing subarray
        length = 1

# update the maximum length of the decreasing subarray
max_length = max(max_length, length)

# print the maximum length of the decreasing subarray
print(max_length)
