

x = int(input('Enter your balance: '))

years = 0
balance = 100

while balance < x:
    balance += balance // 100
    years += 1

print('It will take {} years to double your balance'.format(years))
