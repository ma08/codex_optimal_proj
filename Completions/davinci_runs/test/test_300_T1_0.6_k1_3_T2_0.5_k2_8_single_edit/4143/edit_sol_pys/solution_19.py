

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
    else:
        n = 0
    time += 1
    if n > b:
        n -= b
    else:
        n = 0
    time += 1
    if n > c:
        n -= c
    else:
        n = 0
    time += 1
    if n > d:
        n -= d
    else:
        n = 0
    time += 1
    if n > e:
        n -= e
    else:
        n = 0
    time += 1

print(time)
