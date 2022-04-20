

def ravioli_sort(n, arr, count=0):
    if count == n:
        return arr
    for i in range(count, n):
        if i == n-1:
            return ravioli_sort(n, arr, count+1)
        if abs(arr[i]-arr[i+1]) >= 2:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            return ravioli_sort(n, arr, count+1)

n = int(input())
arr = list(map(int, input().split()))

if ravioli_sort(n, arr) == sorted(arr):
    print("YES")
else:
    print("NO")
