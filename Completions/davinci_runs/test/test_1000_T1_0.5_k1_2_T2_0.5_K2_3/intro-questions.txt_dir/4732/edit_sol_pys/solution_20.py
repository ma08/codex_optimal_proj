
a = int(input())
op = input()
b = int(input())

if op == '+' or op == '-' or op == '*':
    print(eval(str(a)+op+str(b)))
else:
    print('Неизвестная операция')
