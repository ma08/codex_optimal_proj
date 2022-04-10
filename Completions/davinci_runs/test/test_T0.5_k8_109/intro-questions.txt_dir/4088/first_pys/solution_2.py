

# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    m=int(input())
    b=list(map(int,input().split()))
    l=list(s)
    l.sort()
    ans=''
    for i in range(m):
        if(b[i]==0):
            ans+=l[i]
            l.remove(l[i])
        else:
            j=i
            k=b[i]
            while(k>0):
                if(l[j]>l[i]):
                    ans+=l[j]
                    l.remove(l[j])
                    k-=1
                else:
                    j+=1
    print(ans)