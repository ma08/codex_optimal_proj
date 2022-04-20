

# cook your dish here
def find(n,k):
    if n%k==0:
        return n//k
    else:
        return n//k+1

t=int(input())
for i in range(t):
    n,k=map(int,input().split()) # n and k are the number of apples and pieces of apple that can be divided respectively
    print(find(n,k)) # print the number of students
