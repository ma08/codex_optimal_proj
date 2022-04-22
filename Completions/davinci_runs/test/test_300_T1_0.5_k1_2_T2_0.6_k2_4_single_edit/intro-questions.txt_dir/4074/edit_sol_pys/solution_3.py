

# cook your dish here
n=int(input())
s=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if s[i-1]>s[i]:
        if s[i+1]<s[i]:
            c+=1
print(c)
