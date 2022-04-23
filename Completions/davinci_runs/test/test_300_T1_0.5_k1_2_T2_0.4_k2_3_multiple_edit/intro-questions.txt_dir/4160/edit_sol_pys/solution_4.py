

balance = 100
x = int(input("Введите желаемую сумму: "))
year = 0
while balance < x:
    balance += balance // 100
    year += 1
print(year)
