

password, message = input().split()

for i in range(len(password)):  # Перебор символов в пароле
    if message.find(password[i]) == -1:  # Если символа нет в сообщении
        print("FAIL")
        break
    else:
        message = message[message.find(password[i])+1:]  # Удаление всех символов до найденного
else:
    print("PASS")
