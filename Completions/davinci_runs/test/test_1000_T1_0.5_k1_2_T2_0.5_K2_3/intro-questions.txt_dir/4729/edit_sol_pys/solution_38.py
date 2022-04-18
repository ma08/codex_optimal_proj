

password, message = input().split()  # получаем пароль и сообщение

for i in range(len(password)):  # перебираем пароль
    if message.find(password[i]) == -1:  # если в сообщении нет символа из пароля, то пароль не верен
        print("FAIL")
        break
    else:
        message = message[message.find(password[i])+1:]  # иначе удаляем все символы до этого символа
else:
    print("PASS")
