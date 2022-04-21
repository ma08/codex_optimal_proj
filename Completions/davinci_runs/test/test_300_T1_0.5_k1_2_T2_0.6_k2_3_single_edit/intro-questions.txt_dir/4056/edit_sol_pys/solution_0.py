
n,h=map(int,input().split())
a=[0]*n
b=[0]*n
for i in range(n):
  a[i],b[i]=map(int,input().split())
a.sort(reverse=True)
b.sort(reverse=True)
max_a=a[0]
ans=0
for i in range(n):
  if b[i]>max_a:
    h-=b[i]
    ans+=1
    if h<=0:
      print(ans)
      exit()
  else:
    ans+=h//max_a
    if h%max_a==0:
      print(ans)
    else:
      print(ans+1)
    exit()
ans+=h//max_a
if h%max_a==0:
  print(ans)
else:
  print(ans+1)
