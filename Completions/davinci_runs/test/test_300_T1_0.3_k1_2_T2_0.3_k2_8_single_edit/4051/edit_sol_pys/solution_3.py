

def ravioli_sort(arr):
    n = len(arr)
    if n == 1:
        return "YES"
    for i in range(n-1):
        if abs(arr[i]-arr[i+1]) >= 2:
            return "NO"
    return "YES"

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(ravioli_sort(arr))
