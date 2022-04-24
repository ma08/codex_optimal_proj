

def find_max_arr(n, k, i=0):
    if k == 1:
        return [n]
    arr = [1] + [0] * (k-1)
    while arr[i] > arr[i-1] * 2:
        arr[i-1] = arr[i] // 2
    if sum(arr) > n:
        arr[i] -= sum(arr) - n
    if arr[i] == 0:
        return False
    if i == k-1:
        return arr
    return find_max_arr(n, k, i+1)

n, k = [int(x) for x in input().split()]
arr = find_max_arr(n, k, 0)
if arr:
    print("YES")
    print(*arr)
else:
    print("NO")
