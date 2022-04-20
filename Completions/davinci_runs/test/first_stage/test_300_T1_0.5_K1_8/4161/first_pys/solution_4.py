

#-----main-----
n=int(input())

ans=0
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            ans+=gcd(a,b,c)

print(ans)