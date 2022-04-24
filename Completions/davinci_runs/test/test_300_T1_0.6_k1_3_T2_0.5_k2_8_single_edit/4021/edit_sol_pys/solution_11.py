

a = int(input())

x = 1

if a == 0:
    print(1)
else:
    for i in range(a):
        if 2**i <= a < 2**(i + 1):
            x = i + 1

print(x)
