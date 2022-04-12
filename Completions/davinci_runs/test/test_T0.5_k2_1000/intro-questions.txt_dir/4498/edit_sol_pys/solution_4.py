
a, b, c = map(int, input().split())
if a + b == c or a + c == b or b + c == a:
    print('S')
elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
    print('T')
else: print('N')
