

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

time = 0
while n:
    n = max(n-a, 0)
    time+=1
    n = max(n-b, 0)
    time+=1
    n = max(n-c, 0)
    time+=1
    n = max(n-d, 0)
    time+=1
    n = max(n-e, 0)
    time+=1

print(time)
