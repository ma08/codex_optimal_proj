

N=int(input())

i=1
j=1
c=1

while(i*j<N):
    if(i==j):
        j+=1
    else:
        i+=1
    c+=1

print(c)