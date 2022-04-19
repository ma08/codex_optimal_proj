

def ravioli_sort(n, arr, k):
    if n == 1 and arr[0] == k:
        return "YES"
    if n == 1 and arr[0] != k:
        return "NO"
    if n > 1:
        for i in range(n-1):
            if abs(arr[i]-arr[i+1]) >= 2:
                return "NO"
        return "YES"

n = int(input())
k = int(input())
arr = list(map(int, input().split()))

print(ravioli_sort(n, arr, k))
