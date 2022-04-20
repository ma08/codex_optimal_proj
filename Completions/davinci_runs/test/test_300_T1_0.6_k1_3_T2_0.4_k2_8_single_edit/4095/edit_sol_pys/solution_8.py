

def findPairs(arr, n, m):
    count = 0
    for i in range(n):
        for j in range(i, n):
            if m == arr[(i + j) // 2]:
                count += 1
    return count


n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(findPairs(arr, n, m))
