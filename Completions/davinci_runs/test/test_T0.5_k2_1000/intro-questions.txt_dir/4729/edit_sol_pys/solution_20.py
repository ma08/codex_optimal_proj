

def main():
    pass_string, message_string = input().split()  # вводим пароль и сообщение 
    pass_index = 0  # индекс пароля
    for char in message_string:  # проходим по сообщению
        if char == pass_string[pass_index]:  # если символ в сообщении совпадает с символом пароля
            pass_index += 1  # переходим к следующему символу пароля
        if pass_index == len(pass_string):  # если дошли до конца пароля
            print('PASS')  # выводим PASS
            return
    print('FAIL')  # иначе выводим FAIL

if __name__ == "__main__":
    main()
