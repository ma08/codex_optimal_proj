

def findPairs(arr, n, m):
    count = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                count.append([arr[i], arr[j]])
    return len(count)


n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(findPairs(arr, n, m))
