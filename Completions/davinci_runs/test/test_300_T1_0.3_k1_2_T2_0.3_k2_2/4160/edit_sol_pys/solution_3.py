

x = int(input()) # получаем начальный баланс

years = 0
balance = 100

while balance < x: # пока баланс меньше начального
    balance += balance // 100 # добавляем к балансу проценты
    years += 1

print(years)
