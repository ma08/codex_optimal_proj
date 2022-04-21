
n = int(input())
arr = list(map(int, input().split()))

s = input()
total = 0
for i in range(1, n):
    if arr[i] < arr[i-1]:
        total += arr[i-1] - arr[i]
        arr[i] = arr[i-1]
print(total)
