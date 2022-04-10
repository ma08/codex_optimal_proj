

# SOLUTION

n,k = map(int,input().split())
a = list(map(int,input().split()))

if(n==1):
    c = 1
else:
    c = max(a)

if(c<k):
    c = k

x = [0]*(c+1)

for i in a:
    x[i] = x[i] + 1

for i in range(1,c+1):
    if(x[i]>k):
        print("NO")
        exit()

print("YES")

for i in a:
    x[i] = x[i] - 1
    for j in range(1,c+1):
        if(x[j]>0):
            print(j,end=" ")
            x[j] = x[j] - 1
            break