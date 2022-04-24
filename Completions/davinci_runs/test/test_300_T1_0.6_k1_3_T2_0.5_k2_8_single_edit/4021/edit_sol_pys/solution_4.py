


a = int(input())

x = 1

if a == 1:
    print(1)
else:
    for i in range(a):
        if 2**i <= a and a < 2**(i + 1):
            x = i + 1


print(x)
