

def find_min_arr(n, k, arr):
    if k == 0:
        if n == 0:
            return True
        else:
            return False
    if n == 0:
        return True
    if arr[n][k] != -1:
        return arr[n][k]
    if n >= 1 and find_min_arr(n-1, k-1, arr):
        arr[n][k] = 1
        return True
    if n >= 2 and find_min_arr(n-2, k-1, arr):
        arr[n][k] = 2
        return True
    if n >= 3 and find_min_arr(n-3, k-1, arr):
        arr[n][k] = 3
        return True
    if n >= 4 and find_min_arr(n-4, k-1, arr):
        arr[n][k] = 4
        return True
    if n >= 5 and find_min_arr(n-5, k-1, arr):
        arr[n][k] = 5
        return True
    if n >= 6 and find_min_arr(n-6, k-1, arr):
        arr[n][k] = 6
        return True
    arr[n][k] = 0
    return False

n, k = [int(x) for x in input().split()]
arr = [[-1] * (k+1) for _ in range(n+1)]
if find_min_arr(n, k, arr):
    print("YES")
    print(*arr[n][1:])
else:
    print("NO")
