

n, m = [int(x) for x in input().split()]
arr = []

for i in range(n):
    arr.append(input())

for i in range(m):
    l, r = [int(x) for x in input().split()]
    arr = arr[l:r + 1]

print(arr[0])
