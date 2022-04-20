

a,b,c,x = map(int,input().split())
lst = []
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if i*500+j*100+k*50 == x:
                lst.append(i+j+k)
print(min(lst))
