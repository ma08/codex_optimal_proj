

n, k = map(int, input().split())  # количество учеников, количество разбросов
throws = input().split()  # список разбросов

current_student = 0  # начальный номер ученика
current_throw = 0  # начальный номер разброса

while current_throw < k:  # пока не перепрыгнули на последний разброс
    if throws[current_throw].isdigit():  # если разброс числом
        current_student = (current_student + int(throws[current_throw]) % n) % n  # добавляем к номеру ученика разброс
        current_throw += 1  # сдвигаемся вперёд
    else:
        m = int(throws[current_throw][5:])  # количество разбросов назад
        for _ in range(m):  # перебираем разбросы назад
            current_throw -= 1  # сдвигаемся назад
            if throws[current_throw].isdigit():  # если разброс числом
                current_student = (current_student - int(throws[current_throw]) % n) % n  # вычитаем из номера ученика разброс
            else:
                m = int(throws[current_throw][5:])  # количество разбросов назад
                for _ in range(m):  # перебираем разбросы назад
                    current_throw -= 1  # сдвигаемся назад
                    current_student = (current_student + int(throws[current_throw]) % n) % n  # добавляем к номеру ученика разброс

print(current_student)
