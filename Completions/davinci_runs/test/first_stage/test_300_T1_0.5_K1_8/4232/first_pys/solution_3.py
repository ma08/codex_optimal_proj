

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)

if k == 0:
    print(1)
elif k == n:
    print(arr[-1])
else:
    if arr[k-1] == arr[k]:
        print(-1)
    else:
        print(arr[k-1])