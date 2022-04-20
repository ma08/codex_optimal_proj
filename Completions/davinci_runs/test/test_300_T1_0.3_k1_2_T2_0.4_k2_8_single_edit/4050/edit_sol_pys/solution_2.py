
n = int(input())
arr = list(map(float, input().split()))

def solve(n, arr):
    mean = sum(arr) / n
    print(round(mean, 1))
    median = sorted(arr)[n // 2]
    print(round(median, 1))
    mode = max(arr, key=arr.count)
    print(round(mode, 1))

solve(n, arr)
