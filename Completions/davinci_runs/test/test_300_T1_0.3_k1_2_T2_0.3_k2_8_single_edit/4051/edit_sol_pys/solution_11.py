

def ravioli_sort(n, arr, k):
    for i in range(n):
        if arr[i] > k:
            return i
    return n

n = int(input())
arr = list(map(int, input().split()))[:n]
k = int(input())

print(ravioli_sort(n, arr, k))
