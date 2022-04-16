

import itertools 
n=int(input())
l=list(map(int,input().split()))
c=0

for i in range(n):
    for j in range(i+1,n+1):
        t=list(itertools.combinations(l,j))
        for k in t:
            if(all(k[h]<k[h+1] for h in range(len(k)-1))):
                c+=1
print(c)
