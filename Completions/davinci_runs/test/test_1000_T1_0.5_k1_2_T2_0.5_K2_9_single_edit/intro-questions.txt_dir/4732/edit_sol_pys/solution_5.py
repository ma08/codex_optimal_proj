
print('Введите первое число')
a = int(input())
print('Введите операцию')
op = input()
print('Введите второе число')
b = int(input())
print('Результат')
b = int(input())

if op == '+':
    print(a+b)

elif op == '*':

elif op == '-':
    print(a-b)

elif op == '/':
    print(a/b)

elif op == '%':
    print(a%b)

elif op == '//':
    print(a//b)

elif op == '**':
    print(a**b)

else:
    print('Неверная операция')
    print(a*b)
