

def main():
    pass_string = input()
    message_string = input()
    pass_index = 0  # Индекс текущего проверяемого символа пароля
    for char in message_string:  # Проверяем каждый символ в сообщении
        if char == pass_string[pass_index]:
            pass_index += 1  # Увеличиваем индекс пароля
        if pass_index == len(pass_string):
            print('PASS')
            return
    print('FAIL')

if __name__ == "__main__":
    main()
