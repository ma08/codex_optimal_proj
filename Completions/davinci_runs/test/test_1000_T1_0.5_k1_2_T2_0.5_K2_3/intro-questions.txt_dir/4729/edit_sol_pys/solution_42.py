

def main():
    pass_string, message_string = input().split()  # вводим пароль и сообщение
    pass_index = 0  # индекс пароля
    for char in message_string:  # для каждого символа в сообщении
        if char == pass_string[pass_index]:  # если символ в сообщении равен символу в пароле по индексу
            pass_index += 1  # переходим к следующему символу в пароле
        if pass_index == len(pass_string):  # если индекс пароля равен длине пароля
            print('PASS')  # пароль найден
            return
    print('FAIL')  # пароль не найден


if __name__ == "__main__":
    main()
