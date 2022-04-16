
l = [1, 1, 2]
k = int(input())

a = 0
b = 0

if k == 1:
    print(l[0])
elif k == 2:
    print(l[1])
elif k == 3:
    print(l[2])
else:
    for i in range(k-3):
        temp = b
        b = a + b
        a = temp

    print(a+b)
