

n, m = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

for i in range(m):
    l, r = [int(x) for x in input().split()]
    print(min(arr[l:r+1]))
