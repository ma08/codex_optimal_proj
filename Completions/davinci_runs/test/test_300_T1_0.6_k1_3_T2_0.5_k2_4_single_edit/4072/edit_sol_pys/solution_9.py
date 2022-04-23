#input
#conditions
a = int(input())

if a < 100:
    print(0)
elif a % 10 != 0 and a % 100 == 0:
    print(1)
else:
    print(0)
