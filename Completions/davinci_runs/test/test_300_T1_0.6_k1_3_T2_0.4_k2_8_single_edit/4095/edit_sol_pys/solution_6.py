

def findPairs(arr,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return arr[i]

n = int(input())
arr = list(map(int,input().split()))
print(findPairs(arr,n))
