

# SOLUTION
n,k=map(int,input().split())

if k==1:
    if n==1: print("YES\n1")
    else: print("NO")
else:
    if n<k: print("NO")
    else:
        s=n//k
        r=n%k
        if s<2: print("NO")
        else:
            ans=[s]*k
            for i in range(r):
                ans[k-1-i]+=1
            if r==0:
                for i in range(k-1):
                    if ans[i]>=ans[i+1]: print("NO"); break
            else:
                for i in range(k-2):
                    if ans[i]>=ans[i+1]: print("NO"); break
                if ans[k-2]>=ans[k-1]: print("NO")
                else: print("YES\n"+" ".join(map(str,ans)))