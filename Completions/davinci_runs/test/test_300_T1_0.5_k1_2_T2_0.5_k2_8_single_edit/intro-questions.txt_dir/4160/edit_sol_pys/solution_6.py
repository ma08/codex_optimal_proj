

x = int(input('Enter deposit amount: '))
year = 0
balance = 100
while balance < x:
    balance += balance * 0.1
    year += 1
print(year)
