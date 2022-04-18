

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

time = 0
while n:
    n-=a
    if n<0:
        break
    time+=1
    n-=b
    if n<0:
        break
    time+=1
    n-=c
    if n<0:
        break
    time+=1
    n-=d
    if n<0:
        break
    time+=1
    n-=e
    if n<0:
        break
    time+=1

print(time)
