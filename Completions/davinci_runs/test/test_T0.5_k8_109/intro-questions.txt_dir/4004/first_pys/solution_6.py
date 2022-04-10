

def get_min_diff(arr):
    arr = sorted(arr)
    n = len(arr)
    min_diff = float('inf')
    for i in range(n-1):
        min_diff = min(min_diff, arr[i+1] - arr[i])
    return min_diff

n = int(input())
arr = list(map(int, input().split()))
min_diff = get_min_diff(arr)

if min_diff == 0:
    print(0)
elif min_diff == 1:
    print(-1)
else:
    print(min_diff - 1)