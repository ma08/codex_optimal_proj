

x = int(input("Enter a number: "))

years = 0
balance = 100

while balance < x:
    years += 1
    balance += balance * 0.01

print(years)
