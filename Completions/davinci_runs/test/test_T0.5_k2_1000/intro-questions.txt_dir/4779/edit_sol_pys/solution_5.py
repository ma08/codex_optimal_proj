

#%%
n = int(input())
arr = [int(input()) for i in range(n)]

arr.sort()
res = arr[0]*arr[0]*sum(arr[1:]) # max of 3 numbers
for i in range(1,n):
    res = max(res, sum(arr[:i])*sum(arr[i:])) # max of 2 numbers
print(res)
