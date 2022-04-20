

def ravioli_sort(n, arr, k):
    if n == 1:
        return "YES"
    for i in range(n-1):
        if abs(arr[i]-arr[i+1]) > k:
            return "NO"
    return "YES"

n = int(input())
arr = list(map(int, input().split()))

k = int(input())

print(ravioli_sort(n, arr, k))
