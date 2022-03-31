
#-----Solution-----
a = int(input())

if a < 10:
    print(0)
else:
    if a % 10 == 0:
        print(1)
    else:
        print(0)