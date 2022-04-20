
n = int(input())
arr = list(map(int, input().split()))

def solve(n, arr, i=0, j=0):
    if i == n:
        return j
    if arr[i] == 0:
        return solve(n, arr, i+1, j)
    return solve(n, arr, i+1, j+1)

solve(n, arr)
