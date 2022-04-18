

def find_min_arr(n, k, arr):
    for i in range(1, k):
        if n - sum(arr) > arr[i-1]:
            arr[i] = arr[i-1]
        else:
            arr[i] = n - sum(arr)
        if arr[i] == 0: return False
    return True

n, k = [int(x) for x in input().split()]
arr = [1] * k
if find_min_arr(n, k, arr):
    print("YES")
    print(*arr)
else:
    print("NO")
