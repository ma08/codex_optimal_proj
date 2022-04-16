"""Количество подходящих пар"""


def main():
    n = int(input())
    a = list(map(int, input().split()))  # Список половинок пар
    a = list(enumerate(a, 1))  # Нумеруем половинки
    a = sorted(a, key=lambda x: x[1])  # Сортируем половинки по возрастанию
    a = [i[0] for i in a]  # Выбираем индексы половинок
    print(*a, sep='\n')  # Выводим индексы половинок


if __name__ == '__main__':
    main()
