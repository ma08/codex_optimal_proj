
x = int(input())
year = 0
balance = 100
while balance < x:
    balance += balance // 10
    year += 1
print(year)
