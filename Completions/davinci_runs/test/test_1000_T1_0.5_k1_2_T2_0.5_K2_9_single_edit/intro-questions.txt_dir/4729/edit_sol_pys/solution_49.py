

password, message = input().split()  # считываем пароль и последовательность символов

for i in range(len(password)):  # перебираем пароль
    if message.find(password[i]) == -1:  # если в последовательности нет символа из пароля
        print("FAIL")
        break  # завершаем работу
    else:
        message = message[message.find(password[i])+1:]
else:
    print("PASS")
