

name = input()  # вводим имя
new_name = ""  # переменная для нового имени

for i in range(len(name)):  # проходим по всем символам имени
    if i == 0:
        new_name += name[0]
    elif name[i] != name[i-1]:  # если символ не равен предыдущему, то добавляем его в новое имя
        new_name += name[i]

print(new_name)
