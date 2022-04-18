

a = int(input())

if a < 100:
    print(0)
elif a % 10 != 0:
    print(1)
else:
    if a % 100 == 0:
        print(0)
    else:
        print(1)
