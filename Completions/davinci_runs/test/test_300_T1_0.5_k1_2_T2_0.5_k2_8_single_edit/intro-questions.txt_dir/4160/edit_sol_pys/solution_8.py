

x = int(input())
if x > 0:
    year = 0
    balance = 100
    while balance < x:
        balance += balance // 100
        year += 1
    print(year)
else:
    print("Enter a positive number")
