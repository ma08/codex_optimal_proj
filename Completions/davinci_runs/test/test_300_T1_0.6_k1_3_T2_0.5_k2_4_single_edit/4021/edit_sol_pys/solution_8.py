

a = int(input())

x = 1
for i in range(a):
    if 2**i <= a and a < 2**(i + 1):
        x = i + 1

print(x)
