

x = int(input())

years = 0
balance = 100

while balance < x:
    balance *= 1.01
    years += 1

print(years)