
n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
print(arr[n - 1] - arr[0])
