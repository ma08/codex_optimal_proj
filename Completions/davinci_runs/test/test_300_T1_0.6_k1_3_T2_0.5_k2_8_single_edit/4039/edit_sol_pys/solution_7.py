#-----import-----
import sys

#-----main-----
n,r=input().split()
n,r=int(n),int(r)

for i in range(n):
    a,b=input().split()
    a,b=int(a),int(b)
    if r<a:
        print("NO")
        sys.exit()
    r+=b

print("YES")
