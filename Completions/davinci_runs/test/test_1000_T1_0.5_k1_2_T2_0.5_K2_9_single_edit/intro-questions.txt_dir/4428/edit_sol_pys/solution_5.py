

def max_sub_array(arr):
    max_sum = 0
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

n = int(input())
arr = [int(x) for x in input().split()]
print(max_sub_array(arr))
