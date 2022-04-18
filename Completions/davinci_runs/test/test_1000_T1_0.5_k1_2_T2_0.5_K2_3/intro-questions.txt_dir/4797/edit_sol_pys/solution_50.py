def main():
    s = input()
    s_list = []  # список для записи букв
    for i in s:
        if i == '<':  # если встретили знак удаления
            s_list.pop()  # удаляем последний элемент списка
        else:
            s_list.append(i)
    print("".join(s_list))

if __name__ == '__main__':
    main()
