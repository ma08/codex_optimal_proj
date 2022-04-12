

#SOLUTION

b,k,g = map(int,input().split()) #input the value of b, k, g
print(b//g+(1 if b%g else 0)) #print the value of b//g+(1 if b%g else 0)
