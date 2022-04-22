

def find_min_arr(n, k, k_max):
    arr = [1] * k
    for i in range(k_max-1, -1, -1):
        if sum(arr) > n:
            arr[i] -= sum(arr) - n
        if arr[i] == 0:
            return False
        if i == 0:
            break
        if arr[i] > arr[i-1] * 2:
            arr[i-1] = arr[i] // 2
    return arr

n, k = [int(x) for x in input().split()]
k_max = k
while arr is None:
    k_max -= 1
    arr = find_min_arr(n, k, k_max)
if arr:
    print("YES")
    print(*arr)
else:
    print("NO")
