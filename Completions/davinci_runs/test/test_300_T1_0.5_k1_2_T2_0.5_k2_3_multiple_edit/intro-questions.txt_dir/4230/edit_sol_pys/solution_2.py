
a = int(input().split()[1])
b = int(input().split()[1])
c = int(input().split()[1])
d = int(input().split()[1])

if a <= c and b >= d:
    print(0)
elif a <= c and b <= d:
    print(d-b)
elif a >= c and b >= d:
    print(a-c)
else:
    print(a-c + d-b)
