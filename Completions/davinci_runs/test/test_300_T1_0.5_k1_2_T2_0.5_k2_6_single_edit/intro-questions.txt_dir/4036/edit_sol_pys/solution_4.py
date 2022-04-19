

def find_min_arr(n, k, arr=[]):
    if k == 0:
        return arr
    for i in range(1, n+1):
        if i > n:
            return False
        if find_min_arr(n-i, k-1, arr + [i]):
            return arr + [i]

n, k = [int(x) for x in input().split()]
arr = find_min_arr(n, k)
if arr:
    print("YES")
    print(*arr)
else:
    print("NO")
