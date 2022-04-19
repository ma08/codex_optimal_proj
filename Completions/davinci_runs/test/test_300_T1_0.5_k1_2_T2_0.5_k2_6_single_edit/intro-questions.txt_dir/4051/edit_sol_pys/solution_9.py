
import math
import sys

n = int(input())
arr = list(map(float, input().split()))

def mean(arr):
    return sum(arr) / len(arr)

def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]) / 2
    else:
        return arr[(len(arr) // 2) + 1]

def mode(arr):
    arr.sort()
    mode = arr[0]
    max_count = 1
    for i in range(1, len(arr)):
        curr_count = 1
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                curr_count += 1
        if curr_count > max_count:
            max_count = curr_count
            mode = arr[i]
    return mode

def standard_deviation(arr):
    mean_of_arr = mean(arr)
    return math.sqrt(sum([(arr[i] - mean_of_arr) ** 2 for i in range(len(arr))]) / len(arr))

print(round(standard_deviation(arr), 1))
