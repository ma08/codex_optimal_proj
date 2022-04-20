


def deposit_profit(deposit, rate, threshold):
    years = 0
    balance = deposit

    while balance < threshold:
        balance += balance // 100 * rate
        years += 1

    return years


x = int(input())

print(deposit_profit(100, 20, 170))
