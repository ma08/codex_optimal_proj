

x = int(input('Введите сумму: '))

years = 0
balance = 100

while balance < x:
    years += 1
    balance += balance * 0.01

print('Вам потребуется {} лет для накопления суммы {}'.format(years, x))
