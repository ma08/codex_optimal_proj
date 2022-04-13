n = int(input())
arr = [int(x) for x in input().split()]

curr_min = min(arr)
curr_max = max(arr)

print(curr_max - curr_min -
      2*min(curr_max - curr_min, min(arr.count(curr_min), arr.count(curr_max))))
