

def main():
    n,m,x=map(int,input().split())
    c=[0]*n
    a=[]
    for i in range(n):
        c[i],*a=map(int,input().split())+[0]*(m+1)
        a=[0]*m
    ans=10**9
    for i in range(1,1<<n):
        cost=0
        algo=[0]*m
        for j in range(n):
            if i>>j&1:
                cost+=c[j]
                for k in range(m):
                    algo[k]+=a[j][k]
        if min(algo)>=x:
            ans=min(ans,cost)
    if ans==10**9:
        print(-1)
    else:
        print(ans)

if __name__=='__main__':
    main()
