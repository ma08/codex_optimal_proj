
n = int(input("n="))
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))
e = int(input("e="))

time = 0
while n:
    if n>a:
        n-=a
    else:
        n=0
    time+=1
    if n>b:
        n-=b
    else:
        n=0
    time+=1
    if n>c:
        n-=c
    else:
        n=0
    time+=1
    if n>d:
        n-=d
    else:
        n=0
    time+=1
    if n>e:
        n-=e
    else:
        n=0
    time+=1

print(time)
