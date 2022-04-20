


def deposit_calculator(deposit):
    years = 0
    balance = 100

    while balance < deposit:
        balance += balance // 100
        years += 1

    return years


x = int(input())

print(deposit_calculator(x))
