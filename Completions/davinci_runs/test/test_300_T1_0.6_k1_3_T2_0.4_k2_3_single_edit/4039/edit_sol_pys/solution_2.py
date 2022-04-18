

#-----main-----
n,r=input().split()
n,r=int(n),int(r)
if n==0:
    print("YES")
    exit()
else:
    for i in range(n):
        a,b=input().split()
        a,b=int(a),int(b)
        if r<a:
            print("NO")
            exit()
        r+=b

print("YES")
