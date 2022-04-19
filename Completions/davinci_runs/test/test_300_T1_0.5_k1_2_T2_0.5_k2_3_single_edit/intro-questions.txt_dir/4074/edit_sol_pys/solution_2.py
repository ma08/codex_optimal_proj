

# cook your dish here
def find(n,k):
    return (n+k-1)//k

test=int(input())
for i in range(test):
    n,k=map(int,input().split())
    print(find(n,k))
