

x = int(input('Введите число: '))

def f(x):
    year = 0
    balance = 100
    while balance < x:
        balance += balance // 100
        year += 1
    return year

print(f(x))
