

def ravioli_sort(n, arr):
    if n == 1:
        return "YES"
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) >= 2:
            return "NO"

    return "YES"

n = int(input())
arr = list(map(int, input().split()))

print(ravioli_sort(n, arr))
