
n = int(input()) # 2
arr = list(map(int, input().split())) # 1 2
print(all(arr[i]>arr[i-1] for i in range(1,n))) # True
