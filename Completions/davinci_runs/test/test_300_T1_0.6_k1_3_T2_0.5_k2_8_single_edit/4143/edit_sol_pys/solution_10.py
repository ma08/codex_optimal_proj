

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

time = 0
while n:
    if n > a:
        n -= a
    elif n > b:
        n -= b
    elif n > c:
        n -= c
    elif n > d:
        n -= d
    elif n > e:
        n -= e
    time += 1

print(time)
