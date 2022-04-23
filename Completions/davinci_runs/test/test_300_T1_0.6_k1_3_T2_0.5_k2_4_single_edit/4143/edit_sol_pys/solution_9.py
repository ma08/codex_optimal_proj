
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
        time += 1
    elif n > b:
        n -= b
        time += 1
    elif n > c:
        n -= c
        time += 1
    elif n > d:
        n -= d
        time += 1
    elif n > e:
        n -= e
        time += 1
    else: n = 0

print(time)
