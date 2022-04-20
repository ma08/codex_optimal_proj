

a = int(input())

if a % 10 == a // 100 or a % 10 == a // 10 % 10 or a // 10 % 10 == a // 100:
    print(1)
else:
    print(0)
