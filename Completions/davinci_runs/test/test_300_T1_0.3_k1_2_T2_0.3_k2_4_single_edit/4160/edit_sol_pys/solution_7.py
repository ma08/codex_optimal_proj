

x = int(input("Введите сумму вклада: "))

years = 0
balance = 100

while balance < x:
    years += 1
    balance += balance * 0.01

print("Вы получите сумму вклада в течении: ", years, "лет")
