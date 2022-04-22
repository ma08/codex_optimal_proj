
from functools import reduce
import sys

n = int(input())
arr = list(map(int, input().split()))

def sort_ravioli(a, b):
    if a > b:
        return 1
    else:
        return 0

def check_ravioli_sort(arr):
    if sort_ravioli(arr) == sorted(arr):
        return "YES"
    else:
        return "NO"

print(check_ravioli_sort(arr))
