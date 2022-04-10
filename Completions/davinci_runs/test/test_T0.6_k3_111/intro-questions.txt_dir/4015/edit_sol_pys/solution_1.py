

n,m=map(int,input().split())
if(m%n==0 and (m/n)%2==0):
    print(1)
elif(m%n==0):
    print(2)
elif(m%n!=0 and (m/n)%2!=0):
    print(3)
else:
    print(-1)
