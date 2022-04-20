

a = int(input())

x = 1

if a == 1:
    print(1)
else:
    for i in range(1, a + 1):
        if 2**i <= a:
            x = i

print(x)
