

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

time = 0
while n:
    n = n - a if n > a else 0
    time += 1
    n = n - b if n > b else 0
    time += 1
    n = n - c if n > c else 0
    time += 1
    n = n - d if n > d else 0
    time += 1
    n = n - e if n > e else 0
    time += 1

print(time)
