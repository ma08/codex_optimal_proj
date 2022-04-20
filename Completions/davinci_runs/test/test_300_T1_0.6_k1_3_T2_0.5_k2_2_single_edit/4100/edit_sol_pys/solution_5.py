
n,k,q=map(int,input().split())
A=[k]*n
for i in range(q):A[int(input())-1]-=1
for i in A:print("Yes" if i>0 else "No")
