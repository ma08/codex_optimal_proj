

#%%
n = int(input())
arr = [int(input()) for i in range(n)]

arr.sort()
res = arr[0]*arr[0]*sum(arr[1:]) # first term
for i in range(1,n):
    res = max(res, sum(arr[:i])*sum(arr[i:])) # second term
print(res)
