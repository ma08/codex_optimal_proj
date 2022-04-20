


def depositProfit(deposit, rate, threshold):
    year = 0
    balance = deposit
    while balance < threshold:
        balance += balance // 100 * rate
        year += 1
    return year
