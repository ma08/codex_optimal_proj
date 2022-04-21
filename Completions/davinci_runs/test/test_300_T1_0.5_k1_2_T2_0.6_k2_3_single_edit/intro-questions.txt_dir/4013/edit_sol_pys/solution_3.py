n = int(input())  # take input
arr = [int(x) for x in input().split()]
curr_min = min(arr)  # finding min value in arr
curr_max = max(arr)  # finding max value in arr
print(curr_max - curr_min - 2*min(curr_max - curr_min, min(arr.count(curr_min), arr.count(curr_max))))  # print answer
