

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

time = 0
while n:
    n = n - min(n, a)
    time += 1
    n = n - min(n, b)
    time += 1
    n = n - min(n, c)
    time += 1
    n = n - min(n, d)
    time += 1
    n = n - min(n, e)
    time += 1

print(time)
