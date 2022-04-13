

n, k = map(int, input().split())  # количество учеников, количество команд
throws = input().split()  # список команд

current_student = 0  # начальный номер ученика
current_throw = 0  # начальный номер команды

while current_throw < k:  # пока не перепрыгнули на последнюю команду
    if throws[current_throw].isdigit():  # если команда числом
        current_student = (current_student + int(throws[current_throw]) % n) % n  # добавляем к номеру ученика команду
        current_throw += 1  # сдвигаемся вперёд
    else:
        m = int(throws[current_throw][5:])  # количество команд назад
        for _ in range(m):  # перебираем команды назад
            current_throw -= 1  # сдвигаемся назад
            if throws[current_throw].isdigit():  # если команда числом
                current_student = (current_student - int(throws[current_throw]) % n) % n  # вычитаем из номера ученика команду
            else:
                m = int(throws[current_throw][5:])  # количество команд назад
                for _ in range(m):  # перебираем команды назад
                    current_throw -= 1  # сдвигаемся назад
                    current_student = (current_student + int(throws[current_throw]) % n) % n  # добавляем к номеру ученика команду

print(current_student)
