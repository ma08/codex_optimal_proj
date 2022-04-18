

def find_min_arr(n):
    if n == 1:
        return False
    arr = [1] * n
    for i in range(n-1, -1, -1):
        if sum(arr) > n:
            arr[i] -= sum(arr) - n - 1
        if arr[i] == 0:
            arr[i] += 1
            arr[i-1] -= 1
        if arr[i] > arr[i-1] * 2:
            arr[i-1] = arr[i] // 2
        if i == 0 and sum(arr) > n:
            return False
    return arr[:-1]

n = int(input())
arr = find_min_arr(n)
if arr:
    print("YES")
    print(*arr)
else:
    print("NO")
