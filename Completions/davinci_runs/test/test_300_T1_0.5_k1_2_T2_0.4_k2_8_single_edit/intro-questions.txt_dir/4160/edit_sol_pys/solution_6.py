


def func(x):
    year = 0
    balance = 100
    while balance < x:
        balance += balance // 100
        year += 1
    return year


print(func(int(input())))
