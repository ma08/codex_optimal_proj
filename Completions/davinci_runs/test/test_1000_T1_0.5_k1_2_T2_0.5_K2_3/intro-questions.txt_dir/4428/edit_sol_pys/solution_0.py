

def split_array(arr, n):
    sum_arr = sum(arr)
    left_sum = 0
    right_sum = sum_arr
    for i in range(len(arr)):
        right_sum -= arr[i]
        if left_sum == right_sum:
            return left_sum
        left_sum += arr[i]
    return 0

n = int(input())
arr = [int(x) for x in input().split()]
print(split_array(arr, n))
