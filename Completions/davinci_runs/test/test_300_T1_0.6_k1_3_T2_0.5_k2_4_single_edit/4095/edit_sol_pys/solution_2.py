

def findPairs(arr, n, m):
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if m == arr[i] + arr[j]:
                ans += 1
    return ans


n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(findPairs(arr, n, m))
