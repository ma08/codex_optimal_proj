

#Solution:

n,k=map(int,input().split())
s=input()
l=[]
for i in range(n):
    for j in range(i+1,n+1):
        l.append(s[i:j])
l.sort(key=len)
s=set()
c=0
for i in l:
    if len(s)==k:
        break
    if i not in s:
        s.add(i)
        c+=n-len(i)
if len(s)==k:
    print(c)
else:
    print(-1)