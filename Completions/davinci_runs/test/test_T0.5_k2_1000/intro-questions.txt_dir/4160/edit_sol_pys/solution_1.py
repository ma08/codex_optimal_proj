

def main():
    x = int(input())  # задаем количество денег
    count = 0
    balance = 100  # начальный баланс
    while balance < x:  # пока баланс меньше нужного количества денег
        count += 1
        balance += 1  # прибавляем к балансу 1 деньгу

    print(count)

if __name__ == '__main__':
    main()
