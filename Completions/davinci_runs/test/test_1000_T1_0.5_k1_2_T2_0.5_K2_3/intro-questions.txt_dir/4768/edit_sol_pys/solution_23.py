

def main():

    n, k = map(int, input().split())  # n - количество дней, k - количество клиентов
    dna = [input() for i in range(n)]  # список дней
    dna_dict = {}  # словарь дней

    for i in range(n):  # перебор дней
        for j in range(i+1, n):  # перебор дней
            count = 0
            for x in range(k):  # перебор клиентов
                if dna[i][x] != dna[j][x]:  # сравнение клиентов
                    count += 1
            dna_dict[(i+1, j+1)] = count  # добавление дней в словарь

    print(min(dna_dict.values()))  # вывод минимального числа несовпадений

    for key, value in dna_dict.items():  # перебор дней в словаре
        if value == min(dna_dict.values()):  # поиск минимального числа несовпадений
            print(*key)  # вывод номеров дней


if __name__ == '__main__':
    main()
