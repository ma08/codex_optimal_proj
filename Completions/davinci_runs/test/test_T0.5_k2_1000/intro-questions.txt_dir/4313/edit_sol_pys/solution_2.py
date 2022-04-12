
def main():
    n = int(input())
    values = [int(x) for x in input().split()]  # значения предметов
    costs = [int(x) for x in input().split()]  # стоимость предметов
    max_value = 0
    for i in range(1, 2 ** n):  # перебираем все возможные наборы предметов
        value = 0
        cost = 0
        for j in range(n):
            if ((i >> j) & 1):  # если j-й предмет в наборе
                value += values[j]
                cost += costs[j]
        max_value = max(max_value, value - cost)
    print(max_value)


if __name__ == '__main__':
    main()
