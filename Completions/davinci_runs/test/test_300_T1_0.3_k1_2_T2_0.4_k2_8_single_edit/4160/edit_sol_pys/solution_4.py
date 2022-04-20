

x = int(input("Enter the amount of money you want to save: "))

years = 0
balance = 0

while balance <= x:
    years += 1
    balance += 100

print(years)
