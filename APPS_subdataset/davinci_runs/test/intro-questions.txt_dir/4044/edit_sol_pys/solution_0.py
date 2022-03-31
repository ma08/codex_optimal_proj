

a,b,x=map(int,input().split())
if a>b:
    a,b=b,a
if x>a:
    if x==1:
        print("0"*(a+b-1)+"1")
    else:
        print("0"*(a-x)+"1"*(b+x))
elif x<a:
    if x==1:
        print("0"*(a+b-1)+"1")
    else:
        print("0"*(a-x)+"1"*(b+x))
else:
    print("1"*(a+b))
