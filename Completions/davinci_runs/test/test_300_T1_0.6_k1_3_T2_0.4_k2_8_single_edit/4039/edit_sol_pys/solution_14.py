
#-----main-----
n,r=input().split()
n,r=int(n),int(r)

for i in range(n):
    a,b=input().split()
    a,b=int(a),int(b)
    if r<a: #r<aならば絶対にゴールできない
        print("NO")
        exit() #終了
    r+=b

print("YES")
