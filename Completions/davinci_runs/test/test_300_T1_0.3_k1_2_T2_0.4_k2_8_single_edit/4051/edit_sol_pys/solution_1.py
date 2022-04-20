

def ravioli_sort(n, arr, k):
    if n == 0:
        return 0
    if n == 1 and arr[0] == k:
        return 1
    if n == 1 and arr[0] != k:
        return 0
    if n == 2 and arr[0] == k and arr[1] == k:
        return 1
    if n == 2 and arr[0] == k and arr[1] != k:
        return 1
    if n == 2 and arr[0] != k and arr[1] == k:
        return 1
    if n == 2 and arr[0] != k and arr[1] != k:
        return 0
    if n == 3 and arr[0] == k and arr[1] == k and arr[2] == k:
        return 1
    if n == 3 and arr[0] == k and arr[1] == k and arr[2] != k:
        return 1
    if n == 3 and arr[0] == k and arr[1] != k and arr[2] == k:
        return 1
    if n == 3 and arr[0] != k and arr[1] == k and arr[2] == k:
        return 1
    if n == 3 and arr[0] == k and arr[1] != k and arr[2] != k:
        return 1
    if n == 3 and arr[0] != k and arr[1] == k and arr[2] != k:
        return 1
    if n == 3 and arr[0] != k and arr[1] != k and arr[2] == k:
        return 1
    if n == 3 and arr[0] != k and arr[1] != k and arr[2] != k:
        return 0
    if n == 4 and arr[0] == k and arr[1] == k and arr[2] == k and arr[3] == k:
        return 1
    if n == 4 and arr[0] == k and arr[1] == k and arr[2] == k and arr[3] != k:
        return 1
    if n == 4 and arr[0] == k and arr[1] == k and arr[2] != k and arr[3] == k:
        return 1
    if n == 4 and arr[0] == k and arr[1] != k and arr[2] == k and arr[3] == k:
        return 1
    if n == 4 and arr[0] != k and arr[1] == k and arr[2] == k and arr[3] == k:
        return 1
    if n == 4 and arr[0] == k and arr[1] == k and arr[2] != k and arr[3] != k:
        return 1
    if n == 4 and arr[0] == k and arr[1] != k and arr[2] == k and arr[3] != k:
        return 1
    if n == 4 and arr[0] == k and arr[1] != k and arr[2] != k and arr[3] == k:
        return 1
    if n == 4 and arr[0] != k and arr[1] == k and arr[2] == k and arr[3] != k:
        return 1
    if n == 4 and arr[0] != k and arr[1] == k and arr[2] != k and arr[3] == k:
        return 1
    if n == 4 and arr[0] != k and arr[1] != k and arr[2] == k and arr[3] == k:
        return 1
    if n == 4 and arr[0] == k and arr[1] != k and arr[2] != k and arr[3] != k:
        return 1
    if n == 4 and arr[0] != k and arr[1] == k and arr[2] != k and arr[3] != k:
        return 1
    if n == 4 and arr[0] != k and arr[1] != k and arr[2] == k and arr[3] != k:
        return 1
    if n == 4 and arr[0] != k and arr[1] != k and arr[2] != k and arr[3] == k:
        return 1
    if n == 4 and arr[0] != k and arr[1] != k and arr[2] != k and arr[3] != k:
        return 0
    if n == 5 and arr[0] == k and arr[1] == k and arr[2] == k and arr[3] == k and arr[4] == k:
        return 1
    if n == 5 and arr[0] == k and arr[1] == k and arr[2] == k and arr[3] == k and arr[4] != k:
        return 1
    if n == 5 and arr[0] == k and arr[1] == k and arr[2] == k and arr[3] != k and arr[4] == k:
        return 1
    if n == 5 and arr[0] == k and arr[1] == k and arr[2] != k and arr[3] == k and arr[4] == k:
        return 1
    if n == 5 and arr[0] == k and arr[1] != k and arr[2] == k and arr[3] == k and arr[4] == k:
        return 1
    if n == 5 and arr[0] != k and arr[1] == k and arr[2] == k and arr[3] == k and arr[4] == k:
        return 1
    if n == 5 and arr[0] == k and arr[1] == k and arr[2] == k and arr[3] != k and arr[4] != k:
        return 1
    if n == 5 and arr[0] == k and arr[1] == k and arr[2] != k and arr[3] == k and arr[4] != k:
        return 1
    if n == 5 and arr[0] == k and arr[1] != k and arr[2] == k and arr[3] == k and arr[4] != k:
        return 1
    if n == 5 and arr[0] != k and arr[1] == k and arr[2] == k and arr[3] == k and arr[4] != k:
        return 1
    if n == 5 and arr[0] == k and arr[1] == k and arr[2] != k and arr[3] != k and arr[4] == k:
        return 1
    if n == 5 and arr[0] == k and arr[1] != k and arr[2] == k and arr[3] != k and arr[4] == k:
        return 1
    if n == 5 and arr[0] != k and arr[1] == k and arr[2] == k and arr[3] != k and arr[4] == k:
        return 1
    if n == 5 and arr[0] == k and arr[1] != k and arr[2] != k and arr[3] == k and arr[4] == k:
        return 1
    if n == 5 and arr[0] != k and arr[1] == k and arr[2] != k and arr[3] == k and arr[4] == k:
        return 1
    if n == 5 and arr[0] != k and arr[1] != k and arr[2] == k and arr[3] == k and arr[4] == k:
        return 1
    if n == 5 and arr[0] == k and arr[1] == k and arr[2] != k and arr[3] != k and arr[4] != k:
        return 1
    if n == 5 and arr[0] == k and arr[1] != k and arr[2] == k and arr[3] != k and arr[4] != k:
       

n = int(input())
arr = list(map(int, input().split()))

print(ravioli_sort(n, arr))
