

x = int(input())  # получаем количество денег

years = 0  # количество лет
balance = 100  # начальный баланс

while balance < x:  # пока не достигнем нужного баланса
    balance += balance // 100  # добавляем процент от баланса
    years += 1  # увеличиваем количество лет

print(years)  # выводим количество лет
