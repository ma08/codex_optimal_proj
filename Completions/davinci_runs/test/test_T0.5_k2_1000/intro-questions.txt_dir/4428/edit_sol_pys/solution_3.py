

def split_array(array):
    sum_array = sum(array)
    left_sum = 0
    right_sum = sum_array
    for i in range(len(array)):
        right_sum -= array[i]
        if left_sum == right_sum:
            return left_sum
        left_sum += array[i]
    return 0

n = int(input())
arr = [int(x) for x in input().split()]
print(split_array(arr))
