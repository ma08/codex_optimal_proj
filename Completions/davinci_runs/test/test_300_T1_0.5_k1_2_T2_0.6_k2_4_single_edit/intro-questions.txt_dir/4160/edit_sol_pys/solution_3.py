


def year_of_deposit():
    x = int(input())
    year = 0
    balance = 100
    while balance < x:
        balance += balance // 100
        year += 1
    print(year)

year_of_deposit()
