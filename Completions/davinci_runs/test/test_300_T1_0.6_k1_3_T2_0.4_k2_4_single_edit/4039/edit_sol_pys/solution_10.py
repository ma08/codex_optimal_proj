
#----input-----
#-----main-----
n,r=input().split()
n,r=int(n),int(r)
#-----main-----

for i in range(n):
    a,b=input().split()
    a,b=int(a),int(b)
    if r<a:
        print("NO")
        exit()
    r+=b

print("YES")
