

#-----main-----
n,r=input().split()
n,r=int(n),int(r)
ans=True
for i in range(n):
    a,b=input().split()
    a,b=int(a),int(b)
    if r<a:
        ans=False
        break
    r+=b

if ans:
    print("YES")
else:
    print("NO")
