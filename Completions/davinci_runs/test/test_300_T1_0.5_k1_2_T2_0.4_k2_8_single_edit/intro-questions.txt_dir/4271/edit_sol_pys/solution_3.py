
n = int(input()) # number of elements in the array
arr = list(map(int, input().split())) # array elements
arr.sort() # sort the array
for i in range(n):
    print(arr[i], end=' ') # print the array elements
