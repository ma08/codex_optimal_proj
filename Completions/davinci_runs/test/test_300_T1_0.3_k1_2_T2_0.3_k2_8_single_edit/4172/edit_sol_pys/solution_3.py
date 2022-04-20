

def min_moves(arr, k, n):
    if n == 1:
        return 0
    arr.sort(reverse=True)
    if arr[0] - arr[-1] >= k:
        return -1 
    for i in range(n-1):
        if arr[i] - arr[i+1] >= k:
            return -1
    return arr[0] - arr[-1]

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_moves(arr, k, n))
