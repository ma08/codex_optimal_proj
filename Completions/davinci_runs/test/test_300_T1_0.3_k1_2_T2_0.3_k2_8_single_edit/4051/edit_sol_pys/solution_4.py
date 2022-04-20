

def ravioli_sort(n, arr, d):
    for i in range(n):
        if arr[i] > d:
            return i
    return -1

n, d = map(int, input().split())
arr = list(map(int, input().split()))[:n]

print(ravioli_sort(n, arr, d))
