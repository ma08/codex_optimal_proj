# Задача №3.

x = int(input())
year = 0
balance = 100
while balance < x:
    balance += balance / 100
    year += 1

# Задача №4.

a = int(input())
b = int(input())
c = int(input())
if a + b == c:
    print(str(a) + '+' + str(b) + '=' + str(c))
elif a - b == c:
    print(str(a) + '-' + str(b) + '=' + str(c))
elif a * b == c:
    print(str(a) + '*' + str(b) + '=' + str(c))
elif a / b == c:
    print(str(a) + '/' + str(b) + '=' + str(c))
elif a == b + c:
    print(str(a) + '=' + str(b) + '+' + str(c))
elif a == b - c:
    print(str(a) + '=' + str(b) + '-' + str(c))
elif a == b * c:
    print(str(a) + '=' + str(b) + '*' + str(c))
elif a == b / c:
    print(str(a) + '=' + str(b) + '/' + str(c))

# Задача №5.

a = int(input())
b = int(input())
c = int(input())
if a == b or b == c or a == c:
    print('YES')
else:
    print('NO')

# Задача №6.

a = int(input())
b = int(input())
c = int(input())
if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
elif c <= a and c <= b:
    print(c)
print(year)
