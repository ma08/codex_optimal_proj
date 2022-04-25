

x = int(input())  # вводим сумму с клавиатуры 
year = 0
balance = 100
while balance < x:
    balance += balance // 100  # вычисляем сумму вклада без процентов
    year += 1
print(year)
