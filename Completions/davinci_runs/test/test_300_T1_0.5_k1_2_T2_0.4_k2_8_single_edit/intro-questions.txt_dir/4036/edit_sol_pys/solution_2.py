

def find_min_arr(n, k, arr=None):
    if arr is None:
        arr = [1] * k
    if sum(arr) == n:
        return arr
    if sum(arr) > n:
        return False
    for i in range(k-1, -1, -1):
        if arr[i] == 0:
            continue
        arr[i] *= 2
        result = find_min_arr(n, k, arr)
        if result:
            return result
        arr[i] //= 2

n, k = [int(x) for x in input().split()]
result = find_min_arr(n, k)
if result:
    print("YES")
    print(*result)
else:
    print("NO")
