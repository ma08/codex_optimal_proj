
import sys
n=int(sys.stdin.readline())
a=[int(i) for i in sys.stdin.readline().split()]

l=[]
r=[]
ans=[]

for i in a:
    if len(l)==0 or i>l[-1]:
        l.append(i)
    else:
        r.append(i)

while len(l)>0:
    ans.append(l.pop())
    if len(r)>0:
        ans.append(r.pop())

print(len(ans))
for i in ans:
    if i==l[-1]:
        print("L",end="")
    else:
        print("R",end="")