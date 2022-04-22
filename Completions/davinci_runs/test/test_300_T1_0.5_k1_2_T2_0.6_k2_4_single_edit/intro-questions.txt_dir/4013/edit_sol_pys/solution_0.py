
n = int(input())
arr = [int(x) for x in input().split()]

current_min = min(arr)
current_max = max(arr)

print(current_max - current_min - 2*min(current_max - current_min, min(arr.count(current_min), arr.count(current_max))))
