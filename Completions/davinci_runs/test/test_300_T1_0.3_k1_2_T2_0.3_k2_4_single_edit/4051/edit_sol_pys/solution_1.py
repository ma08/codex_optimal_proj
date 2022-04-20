

def ravioli_sort(n, arr, k):
    for i in range(n):
        if abs(arr[i]-arr[i+1]) >= k:
            return "NO"
    return "YES" if n > 0 else "NO"

n = int(input())
k = int(input())
arr = [int(input()) for i in range(n)]

print(ravioli_sort(n, arr, k))
