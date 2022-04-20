

def findPairs(arr,n):
    arr.sort()
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            return arr[i]
    return -1

n = int(input())
arr = list(map(int,input().split()))
print(findPairs(arr,n))
