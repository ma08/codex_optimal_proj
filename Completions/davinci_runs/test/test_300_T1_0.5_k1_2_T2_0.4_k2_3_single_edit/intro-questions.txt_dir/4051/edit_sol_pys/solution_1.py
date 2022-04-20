
import sys

n = int(input())
arr = list(map(int, input().split()))

def sort_ravioli(arr, n):
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def check_ravioli_sort(arr, n):
    if sort_ravioli(arr, n) == sorted(arr):
        return "YES"
    else:
        return "NO"

print(check_ravioli_sort(arr, n))
