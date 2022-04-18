

def find_max_arr(n, k, arr=None):
    if arr is None:
        arr = [1] * k
    if k == 0:
        return True
    for i in range(k):
        if sum(arr) > n:
            arr[i] = n - sum(arr[:i]) + arr[i]
        if sum(arr) == n:
            return True
        if arr[i] == 0:
            return False
        if arr[i] > arr[i-1] * 2:
            arr[i-1] = arr[i] // 2
    return find_max_arr(n, k-1, arr)

n, k = [int(x) for x in input().split()]
arr = find_max_arr(n, k)
if arr:
    print("YES")
    print(*arr)
else:
    print("NO")
