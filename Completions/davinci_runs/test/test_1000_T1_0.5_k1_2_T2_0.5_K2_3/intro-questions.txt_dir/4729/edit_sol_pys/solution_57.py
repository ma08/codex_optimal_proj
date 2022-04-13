

def main():
    pass_string, message_string = input().split()  # Получаем строки из первой строки ввода.
    pass_index = 0  # Индекс текущего проверяемого символа пароля
    for char in message_string:  # Проверяем каждый символ в сообщении.
        if char == pass_string[pass_index]:  # Если символ совпадает с символом пароля.
            pass_index += 1  # Увеличиваем индекс пароля.
        if pass_index == len(pass_string):  # Если индекс совпадает с длиной пароля.
            print('PASS')  # Печатаем PASS.
            return  # И выходим из функции.
    print('FAIL')  # Если дошли до сюда, то печатаем FAIL.

if __name__ == "__main__":
    main()
