

x = int(input())
years = 0
balance = 100
while balance < x:
    balance += balance // 100
    years += 1
print(years)
