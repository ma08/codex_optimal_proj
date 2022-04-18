

def find_min_arr(n, k, arr):
    for i in range(k-1, 0, -1):
        if sum(arr) > n:
            arr[i] -= sum(arr) - n
        if arr[i] == 0:
            return False
        if i == 0:
            break
        if arr[i] > arr[i-1] * 2:
            arr[i-1] = arr[i] // 2
    return arr


for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    arr = [1] * k
    arr = find_min_arr(n, k, arr)
    if arr:
        print("YES")
        print(*arr)
    else:
        print("NO")
