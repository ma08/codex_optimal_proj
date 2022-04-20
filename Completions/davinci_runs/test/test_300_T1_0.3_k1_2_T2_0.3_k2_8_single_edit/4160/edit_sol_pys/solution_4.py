

x = int(input('Введите число: '))

years = 0
balance = 100

while balance < x:
    balance += balance // 10
    years += 1

print(years)
