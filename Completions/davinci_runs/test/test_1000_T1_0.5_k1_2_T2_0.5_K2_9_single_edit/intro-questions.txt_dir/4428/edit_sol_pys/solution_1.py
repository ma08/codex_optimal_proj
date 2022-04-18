

def split_array(arr):
    sum_arr = 0
    left_sum = 0
    right_sum = 0
        sum_arr += arr[i]
    for i in range(len(arr)):
        right_sum -= arr[i]
        if left_sum == right_sum:
            return left_sum
        left_sum += arr[i]
    return 0

n = int(input())
arr = [int(x) for x in input().split()]
print(split_array(arr))
