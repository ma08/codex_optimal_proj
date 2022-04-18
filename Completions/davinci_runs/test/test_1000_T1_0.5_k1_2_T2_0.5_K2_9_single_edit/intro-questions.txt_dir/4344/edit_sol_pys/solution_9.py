
n=int(input())
l=list(map(int,input().split()))
for i in range(1,len(l)):
    if l[i]!=l[i-1]:
        print(l[i-1],end=" ")
print(l[-1])
