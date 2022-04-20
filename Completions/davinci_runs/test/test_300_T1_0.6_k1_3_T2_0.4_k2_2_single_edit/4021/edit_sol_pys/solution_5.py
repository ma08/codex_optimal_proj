

a = int(input("Enter a number: "))

x = 0

if a == 1:
    print(0)
else:
    for i in range(a):
        if 2**i <= a and a < 2**(i + 1):
            x = i

print(x)
