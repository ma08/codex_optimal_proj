

#SOLUTION

b,k,g = map(int,input().split())
print(b//g+(1 if b%g != 0 else 0))
