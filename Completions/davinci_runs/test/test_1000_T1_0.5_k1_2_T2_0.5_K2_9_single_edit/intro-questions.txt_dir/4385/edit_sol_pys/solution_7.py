

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n=int(input())
s=input()
a=[0]*n
a[0]=1 if s[0]=="#" else 0
for i in range(1,n):
	a[i]=a[i-1]+1 if s[i]=="#" else 0
ans=n
for i in range(n):
	ans=min(ans,a[i]+n-i-1)
print(ans)
