

def depositProfit(deposit, rate, threshold):
    year = 0
    balance = deposit

    while balance < threshold:
        balance += balance * rate / 100
        year += 1
    return year
