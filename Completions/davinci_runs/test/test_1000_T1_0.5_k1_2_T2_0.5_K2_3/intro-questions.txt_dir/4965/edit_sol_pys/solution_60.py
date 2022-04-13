import sys

def rearrange(length, arr):
    arr = sorted(arr)
    if length%2 == 0:
        arr1 = arr[:length//2]
        arr2 = arr[length//2:]
    else:
        arr1 = arr[:length//2]
        arr2 = arr[length//2+1:]
    arr1.reverse()
    arr1 = arr1 + arr2
    return arr1

n = int(input())
arr = [int(x) for x in input().split()]

print(*rearrange(n, arr))
