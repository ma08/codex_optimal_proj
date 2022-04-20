

#-----main-----
n,r=input().split()
n,r=int(n),int(r)
#print(n,r)
for i in range(n):#ここでfor文を回す
    a,b=input().split()
    a,b=int(a),int(b)
    #print(a,b)
    if r<a:#ここで比較をしている
        print("NO")
        exit()
    r+=b

print("YES")
