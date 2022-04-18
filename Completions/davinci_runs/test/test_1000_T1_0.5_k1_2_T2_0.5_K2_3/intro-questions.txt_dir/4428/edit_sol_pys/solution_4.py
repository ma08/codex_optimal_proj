
def splitArray(arr):
    sum_arr = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        if left_sum == sum_arr - left_sum - arr[i]:
            return i
        left_sum += arr[i]
    return 0

n = int(input())
arr = [int(x) for x in input().split()]
print(splitArray(arr))
