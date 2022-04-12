

x = int(input())  # вводим сумму денег для достижения
year = 0
balance = 100  # начальный баланс
while balance < x:  # пока баланс меньше суммы денег для достижения
    balance += balance // 100  # добавляем процент к балансу
    year += 1
print(year)
