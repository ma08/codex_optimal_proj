

def check_password(password, message):  # check if password is in message
    password = list(password)  # convert password to list
    for i in range(len(password)):
        try:
            index = message.index(password[i])  # get index of first occurrence of password character
        except ValueError:
            return "FAIL"  # if character is not in message, return FAIL
        message = message[index+1:]  # remove characters before index of character
    return "PASS"  # if all characters are in message, return PASS

print(check_password(input(), input()))
