from sys import stdin

n = int(input())
a = list(map(int, stdin.readline().split()))

time = 0
while n:
    if n>a[0]:
        n-=a[0]
    else:
        n=0
    time+=1
    if n>a[1]:
        n-=a[1]
    else:
        n=0
    time+=1
    if n>a[2]:
        n-=a[2]
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
