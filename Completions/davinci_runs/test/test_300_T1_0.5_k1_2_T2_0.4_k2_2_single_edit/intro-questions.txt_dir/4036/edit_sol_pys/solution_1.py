

def find_min_arr(n, k, arr):
    for i in range(k - 1, -1, -1):
        if sum(arr) < n:
            arr[i] *= 2
        else:
            arr[i] -= sum(arr) - n
            return arr
    return False

n, k = [int(x) for x in input().split()]
arr = [1] * k
arr = find_min_arr(n, k, arr)
if arr:
    print("YES")
    print(*arr)
else:
    print("NO")
