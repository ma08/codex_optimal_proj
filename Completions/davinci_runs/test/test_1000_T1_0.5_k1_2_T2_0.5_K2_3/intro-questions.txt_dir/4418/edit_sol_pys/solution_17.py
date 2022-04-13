
n = int(input())  # количество чисел в массиве
a = list(map(int, input().split()))  # массив

def find_index(a: list, x: int, start=0):  # поиск индекса числа x в массиве a начиная с start
    for i in range(start, len(a)):
        if a[i] == x:
            return i
    return -1


def delete_numbers(a: list):  # удаление возможных последовательностей чисел
    while True:
        if len(a) == 0:
            return 0
        if len(a) % 6 != 0:  # если длина массива не кратна 6, то выходим
            return len(a)
        if a[0] == 4:  # если первое число массива равно 4
            i = 0
            for x in [8, 15, 16, 23, 42]:  # проходим по всем числам последовательности
                i = find_index(a, x, i + 1)  # поиск индекса найденного числа
                if i == -1:  # если число не найдено, то выходим
                    return len(a)
        else:  # если первое число не равно 4, то выходим
            return len(a)
        a = a[i + 1:]  # удаление найденной последовательности

print(delete_numbers(a))  # вывод оставшихся чисел
