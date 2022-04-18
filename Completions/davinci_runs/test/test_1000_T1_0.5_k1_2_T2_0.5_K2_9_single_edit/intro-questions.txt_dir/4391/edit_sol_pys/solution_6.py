

n,k = map(int, input().split()) # n = number of elements in array a, k = number of elements in subarray
a = list(map(int, input().split())) # a is the array

max_sum = sum(a[:k]) # max_sum is the sum of the first k elements in a
curr_sum = max_sum # curr_sum is the sum of the current subarray
for i in range(k,n):
    curr_sum += a[i] - a[i-k] # curr_sum is the sum of the current subarray
    max_sum = max(max_sum, curr_sum) # max_sum is the maximum sum of the subarrays

print(max_sum/k) # average of the maximum sum of the subarrays
