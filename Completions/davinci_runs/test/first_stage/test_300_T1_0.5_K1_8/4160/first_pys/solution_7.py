

x = int(input())

balance = 100
year = 0

while balance < x:
    balance += balance // 100
    year += 1

print(year)