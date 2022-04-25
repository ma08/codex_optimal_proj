n=int(input())
p,s=[],[]
for i in range(n):
    p.append(input())
for i in range(n):
    s.append(input())
p=sorted(p,key=lambda x:len(x))
s=sorted(s,key=lambda x:len(x))
ans=''
for i in range(n):
    if p[i]==s[i]:
        ans+='P'
    else:
        ans+='S'
for i in range(n-1,-1,-1):
    if p[i]==s[i]:
        ans+='P'
    else:
        ans+='S'
print(ans)
