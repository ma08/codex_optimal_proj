
import sys

n = int(input())
arr = list(map(int, input().split()))

def sort_ravioli(n):
    if n == 1:
        return "YES"
    if n == 2:
        if arr[0] > arr[1]:
            return "YES"
        else:
            return "NO"
    if n == 3:
        if arr[0] > arr[1] and arr[1] > arr[2]:
            return "YES"
        else:
            return "NO"
    if n > 3:
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                return "NO"
        return "YES"


print(sort_ravioli(n))
