

x = int(input('Введите желаемый баланс: '))  # желаемый баланс
year = 0
balance = 100  # начальный баланс
while balance < x:
    balance += balance // 100  # процент
    year += 1
print(year)
