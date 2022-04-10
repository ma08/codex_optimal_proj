

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if(gcd(a,b)==1 and gcd(b,c)==1):
        print(0)
        print(a,b,c)
    else:
        flag=0
        x=gcd(a,b)
        y=gcd(b,c)
        z=gcd(a,c)
        if(x==1):
            if(y==1):
                print(1)
                print(a,b,c)
            else:
                flag=1
        if(y==1):
            if(x==1):
                print(1)
                print(a,b,c)
            else:
                flag=1
        if(flag==0):
            print(2)
            print(x,y,z)