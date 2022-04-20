

a, b = map(int, input().split())
if a * 100 / 8 >= b * 10:
    print(int(b * 10))
elif a * 100 / 8 < a * 10:
    print(int(a * 10))
else:
    print(int(a * 100 // 8))
