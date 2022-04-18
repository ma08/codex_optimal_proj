
a, b, c, d = input().split()  # читаем все числа
color_list = [int(a), int(b), int(c), int(d)]  # делаем из них список
color_list = sorted(color_list)  # сортируем список
i = 0  # начальная позиция списка
while i < len(color_list) - 1:  # пока не дойдем до последнего элемента
    if color_list[i] == color_list[i + 1]:  # если элемент повторяется
        color_list.pop(i)  # удаляем его
        i -= 1  # уменьшаем индекс на 1, т.к. список стал короче
    i += 1  # переходим к следующему элементу
print(len(color_list))  # выводим длину списка
