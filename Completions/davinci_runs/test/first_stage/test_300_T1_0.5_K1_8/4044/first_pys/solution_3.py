

# cook your dish here
a, b, x = map(int, input().split())
if 2*a == x:
    print('0' * a + '1' * b)
elif 2*b == x:
    print('1' * b + '0' * a)
elif x == a + b - 1:
    print('0' * (a - 1) + '10' + '1' * (b - 1))
elif a == b:
    print('1' * (b - 1) + '01' + '0' * (a - 1))
elif a > b:
    print('0' * b + '1' * (a - 1) + '01')
else:
    print('1' * a + '0' * (b - 1) + '10')