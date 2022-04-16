
name = input()  # вводим строку
for i in range(1, len(name)):  # проходим по строке
    if name[i] == name[i - 1]:  # сравниваем элементы попарно
        name = name[:i] + name[i + 1:]  # если совпадают, удаляем один из них
        i -= 1
print(name)  # выводим строку
