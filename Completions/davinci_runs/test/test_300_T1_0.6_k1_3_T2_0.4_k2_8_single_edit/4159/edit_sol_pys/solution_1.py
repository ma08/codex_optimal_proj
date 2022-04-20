
import sys
sys.setrecursionlimit(10**7)


def sol():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()
    B.sort()
    C.sort()

    ans = 0
    for b in B:
        ans += upper_bound(A, b) * lower_bound(C, b)

    print(ans)


def upper_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


def lower_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return len(arr) - left


sol()


'''

A, B, K = map(int, input().split())

if A < K:
    K -= A
    A = 0
    if B < K:
        B = 0
    else:
        B -= K
else:
    A -= K

'''
print(A, B)
