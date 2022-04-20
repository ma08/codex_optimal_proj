

n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
print(arr[-1] - arr[0])
