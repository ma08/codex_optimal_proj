

def find_min_arr(n, k, arr=None):
    if arr is None:
        arr = [1] * k
    if sum(arr) > n:
        return False
    if sum(arr) == n:
        return arr
    if k == 0:
        return False
    for i in range(1, arr[-1] + 1):
        res = find_min_arr(n, k-1, arr + [i])
        if res:
            return res
    return False

n, k = [int(x) for x in input().split()]
arr = find_min_arr(n, k)
if arr:
    print("YES")
    print(*arr)
else:
    print("NO")
