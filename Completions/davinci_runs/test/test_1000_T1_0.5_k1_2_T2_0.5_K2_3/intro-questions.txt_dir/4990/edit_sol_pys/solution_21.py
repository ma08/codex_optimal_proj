

#SOLUTION

b,k,g=map(int,input().split())
print(k//g+(1 if k%g else 0))
