

a, op, b = map(str, input().split())
a = int(a)
b = int(b)
if op == '+':
    if a + b >= 10:
        print('error')
    else:
        print(a + b)
elif op == '-':
    if a - b < 0:
        print('error')
    else:
        print(a - b)
else:
    print('error')
