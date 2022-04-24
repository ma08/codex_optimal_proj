

a = int(input())

if a < 100:
    print(0)
elif a % 10 != 0:
    print(a//100 +1)
else:
    print(a//100)
