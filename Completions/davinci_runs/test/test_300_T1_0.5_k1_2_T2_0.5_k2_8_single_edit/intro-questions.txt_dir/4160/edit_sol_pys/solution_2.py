

x = int(input('Please enter the amount of money to be deposited: '))
year = 0
balance = 100
while balance < x:
    balance += balance // 100
    year += 1
print(f'{year} years')
