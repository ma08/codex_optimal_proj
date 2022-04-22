

x = int(input())  # вводим количество рублей
year = 0
balance = 100  # начальный баланс
while balance < x:  # цикл пока баланс меньше введенного значения
    balance += balance // 100  # прибавляем к балансу процент от баланса
    year += 1
print(year)
