
# cook your code here
def find(n,k,l):
    for i in range(n):
        if l[i]<=k:
            k=k-l[i]
            l[i]=0
        else:
            l[i]=l[i]-k
            k=0
            break
    if k==0:
        return l
    else:
        return -1
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l=find(n,k,l)
    if l==-1:
        print(-1)
    else:
        l.sort()
        print(l[0])
