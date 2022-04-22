
n = int(input())  # number of elements
arr = [int(i) for i in input().split()]
max = arr[0]
min = arr[0]
for i in range(1, n):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]
print(max - min)
