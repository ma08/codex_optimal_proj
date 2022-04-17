# cook your dish here

# cook your dish here
def find(n,k):
    if n%k==0:
        return n//k
    else:
        return n//k+1

t=int(input())
for i in range(t):
    n,k=map(int,input().split(" "))
    print(find(n,k),end="\n")
