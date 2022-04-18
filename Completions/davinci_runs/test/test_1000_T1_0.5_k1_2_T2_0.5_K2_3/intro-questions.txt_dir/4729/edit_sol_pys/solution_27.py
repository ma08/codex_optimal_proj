

def check_password(password, message):
    password = list(password)
    for i in range(len(password)):
        try:
            index = message.index(password[i])
        except ValueError:
            return False
        message = message[index+1:]
    return True

def check_password_2(password, message):
    password = list(password)
    for i in range(len(password)):
        index = message.find(password[i])
        if index == -1:
            return False
        message = message[index+1:]
    return True

print(check_password_2(input(), input()))
