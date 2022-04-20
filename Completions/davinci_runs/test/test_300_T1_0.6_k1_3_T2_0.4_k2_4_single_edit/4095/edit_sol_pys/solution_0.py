

def findPairs(arr, n, m):
    count = 0 
    for i in range(n-1):
        for j in range(i+1,n):
            if m == arr[i] + arr[j]:
                count += 1 
    return count 

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(findPairs(arr, n, m))
