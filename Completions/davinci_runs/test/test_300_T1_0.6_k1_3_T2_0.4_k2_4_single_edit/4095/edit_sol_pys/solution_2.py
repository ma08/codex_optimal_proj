

def findPairs(arr,n):
    # count = 0
    # for i in range(n):
    #     for j in range(i,n):
    #         if m == arr[(i+j)//2]:
    #             count += 1
    # return count
    return sum(arr)

n = int(input())
arr = list(map(int,input().split()))
print(findPairs(arr,n))
