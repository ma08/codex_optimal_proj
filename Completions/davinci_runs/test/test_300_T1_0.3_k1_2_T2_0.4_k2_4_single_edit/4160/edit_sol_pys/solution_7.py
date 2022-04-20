

x = int(input("Enter a number: "))

year = 0
balance = 1000

while balance < x:
    year += 1
    balance += balance * 0.01

print(year)
