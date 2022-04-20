

x = int(input('Enter the sum you want to earn: '))

years = 0
balance = 1000

while balance < x:
    balance += balance // 10
    years += 1

print(years)
