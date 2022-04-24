
import sys
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    m=max(a)
    index=a.index(m)
    if (index>0 and index<n-1):
        if(a[index-1]<a[index] and a[index+1]<a[index]):
            print(a[index])
        else:
            print(-1)
    elif(index>0):
        if(a[index-1]<a[index]):
            print(a[index])
        else:
            print(-1)
    elif(index<n-1):
        if(a[index+1]<a[index]):
            print(a[index])
        else:
            print(-1)
    else:
        print(-1)
