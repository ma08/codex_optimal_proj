#Problem
'''
You are given an array a consisting of n distinct integers. 
You want to know how many pairs (i,j) of indices of this array satisfy the condition ai+aj>x.
'''

#Solution

n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
count=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j]>x:
            count=max(count,i+1)
            break


#alternate solution

n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
count=0
for i in range(n):
    if a[i]>x:
        break
    count+=1
print(count*(count-1)//2)
print(count)
